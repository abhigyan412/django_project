from django.shortcuts import render,HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login
from django.contrib.auth import authenticate, login as auth_login

from django.conf import settings
from .models import Transaction
from .checksum import generate_checksum, verify_checksum
from django.views.decorators.csrf import csrf_exempt
from home.models import Contact
from home.models import signup



def index(request):

    
    
    return render(request,'index.html' )
   
    #return HttpResponse("This is homepage")
def about(request):
    return render(request,'about.html' )
    #return HttpResponse("This is about page")
def services(request):
    return render(request,'services.html')
    #return HttpResponse("This is services page")
def someone(request):
    return render(request,'someone.html')    
def contact(request):
    if request.method == "POST":
        email=request.POST.get('email')
        desc=request.POST.get('desc')
        contact=Contact(email=email , desc=desc)
        contact.save()
        messages.success(request, 'We recieved your communication, we will contact you shortly.')
    
    return render(request,'contact.html')
    #return HttpResponse("This is contact page ")     

def login(request):
    if request.method == "POST":
        contact = request.POST['contact']
        password  = request.POST['password']

        df = authenticate(contact = contact , password = password)

        if df is not None:
            login(request , df )
            return 
        else:
            messages.success(request, 'Invalid credentials.')
            return render(request, 'login.html')


    return render(request,'login.html')        

def signup_view(request):
    if request.method == "POST":
        contact = request.POST.get('contact')
        password = request.POST.get('password')
        df=signup(contact = contact , password =  password)
        if signup.objects.filter(contact = contact).exists():
            messages.success(request, 'Contact already exists please sign in ')   

        else:
         df.save()
         messages.success(request, 'Signed up successfully')   
    
    return render(request ,'signup.html')    

def initiate_payment(request):
    if request.method == "GET":
        return render(request, 'someone.html')
    try:
        username = request.POST['username']
        password = request.POST['password']
        amount = int(request.POST['amount'])
        user = authenticate(request, username=username, password=password)
        if user is None:
            raise ValueError
        auth_login(request=request, user=user)
    except:
        return render(request, 'someone.html', context={'error': 'Wrong Accound Details or amount'})

    transaction = Transaction.objects.create(made_by=user, amount=amount)
    transaction.save()
    merchant_key = settings.PAYTM_SECRET_KEY

    params = (
        ('MID', settings.PAYTM_MERCHANT_ID),
        ('ORDER_ID', str(transaction.order_id)),
        ('CUST_ID', str(transaction.made_by.email)),
        ('TXN_AMOUNT', str(transaction.amount)),
        ('CHANNEL_ID', settings.PAYTM_CHANNEL_ID),
        ('WEBSITE', settings.PAYTM_WEBSITE),
        # ('EMAIL', request.user.email),
        # ('MOBILE_N0', '9911223388'),
        ('INDUSTRY_TYPE_ID', settings.PAYTM_INDUSTRY_TYPE_ID),
        ('CALLBACK_URL', 'http://127.0.0.1:8000/handlerequest/'),
        # ('PAYMENT_MODE_ONLY', 'NO'),
    )

    paytm_params = dict(params)
    checksum = generate_checksum(paytm_params, merchant_key)

    transaction.checksum = checksum
    transaction.save()

    paytm_params['CHECKSUMHASH'] = checksum
    print('SENT: ', checksum)

    return render(request, 'paytm.html', context=paytm_params)


@csrf_exempt
def handlerequest(request):
    if request.method == 'POST':
        received_data = dict(request.POST)
        paytm_params = {}
        paytm_checksum = received_data['CHECKSUMHASH'][0]
        for key, value in received_data.items():
            if key == 'CHECKSUMHASH':
                paytm_checksum = value[0]
            else:
                paytm_params[key] = str(value[0])

        # Verify checksum
        is_valid_checksum = verify_checksum(paytm_params, settings.PAYTM_SECRET_KEY, str(paytm_checksum))
        if is_valid_checksum:
            received_data['message'] = "Checksum Matched"
        else:
            received_data['message'] = "Checksum Mismatched"
            return render(request, 'payments/callback.html', context=received_data)
        return render(request, 'payments/callback.html', context=received_data)        

    
