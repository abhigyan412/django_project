from django.shortcuts import render,HttpResponse
from django.contrib import messages

from home.models import Contact
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