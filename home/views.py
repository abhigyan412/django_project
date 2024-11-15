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
from django.contrib.auth.decorators import login_required
from math import ceil
from  home.models import icecream
from home.models import family
from home.models import mf , Orders , suggestion




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
def suggest(request):
    if request.method == "POST":
        email=request.POST.get('email')
        suggestion1=request.POST.get('suggestion')
        res = suggestion(suggestions = suggestion1 , email=email )
        res.save()
        messages.success(request, 'We welcome your suggestion')
    return render(request,'suggestion.html')    

def quiz(request):
     if request.method == 'POST':
        # Get the form answers from POST data
        answers = {
            'q1': request.POST.get('q1'),
            'q2': request.POST.get('q2'),
            'q3': request.POST.get('q3'),
            'q4': request.POST.get('q4'),
            'q5': request.POST.get('q5')
        }

        result = calculate_flavor(answers)
        return render(request, 'k.html' , {'flavor': result})
     return render(request, 'j.html')


def calculate_flavor(answers):
    # Simple logic to calculate flavor based on answers
    counts = {'A': 0, 'B': 0, 'C': 0, 'D': 0}
    
    for answer in answers.values():
        if answer in counts:
            counts[answer] += 1
    
    # Find the maximum count to determine the flavor
    max_choice = max(counts, key=counts.get)
    
    # Map answers to flavors
    flavor_map = {
        'A': "Lemon Sorbet or Citrus Gelato",
        'B': "Mocha or Double Chocolate Fudge",
        'C': "Strawberry or Berry Swirl",
        'D': "Salted Caramel or Peanut Butter"
    }
    
    return flavor_map.get(max_choice, "Vanilla")  




def login(request):
    if request.method == "POST":
        contact = request.POST.get('contact')
        password  = request.POST.get('password')

        dr = signup.objects.filter(contact=contact)
        ds = signup.objects.filter(password=password)

        if dr.exists() and ds.exists():
            messages.success(request, 'succesfully logged in ')
            return render(request, 'someone.html')
        
        else:
            messages.success(request, 'Invalid credentials.')
            return render(request, 'login.html')


    return render(request,'login.html')        

def signup_view(request):
    if request.method == "POST":
        contact = request.POST.get('contact')
        password = request.POST.get('password')
        dr = signup.objects.filter(contact=contact)
        df=signup(contact = contact , password = password )
        if dr.exists():
            messages.info(request, 'Contact already exists please sign in ')   

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

def icecreams(request):
       products = icecream.objects.all()
       n = len(products)
       print(n)
       nslides = n//3 +ceil((n/3)-(n//3))

       params = {'no_of_slides':nslides,'range':range(1, nslides),'product' : products}
       return  render(request ,'icecream.html' , params )


def fami(request):
       families = family.objects.all()
       r = len(families)
       print(r)
       sr = r//3 +ceil((r/3)-(r//3))

       sf = {'no_of_slides':sr,'range':range(1,sr),'fmly' : families}
       return  render(request ,'family.html' , sf )

def vc(request):
       ves = mf.objects.all()
       t = len(ves)
       print(t)
       vr = t//3 +ceil((t/3)-(t//3))

       vf = {'no_of_slides':vr,'range':range(1,vr),'vy' : ves}
       return  render(request ,'men.html' , vf )


def checkout(request):
       if request.method=="POST": 
        items_json=request.POST.get('itemsJson', '')
        name=request.POST.get('name', '')
        amount=request.POST.get('amount', '')
        email=request.POST.get('email', '')
        address=request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city=request.POST.get('city', '')
        state=request.POST.get('state', '')
        zip_code=request.POST.get('zip_code', '')
        phone=request.POST.get('phone', '')
        
        order = Orders(items_json = items_json , name = name  , amount = amount ,  email = email , address = address , city = city , state = state , zip_code = zip_code , phone =phone)
        order.save()

        thank = True
        id = order.order_id
        return render(request,'checkout.html' , {'thank':thank , 'id':id})
       return render(request,'checkout.html')
