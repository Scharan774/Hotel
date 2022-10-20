from django.shortcuts import render,redirect
from django.contrib import messages
from . models import items
from django.contrib.auth.models import User
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.
l=[]
l1=[]
price=0
def index(request):
    return render(request,'index.html')
def HungryHorse(request):
    if (request.method=='GET'):
        hotel=request.GET['text']
        if hotel=='HungryHorse':
            features=items.objects.all()
            return render(request,'HungryHorse.html',{'features':features})
def HungryHorse1(request):
    hotel='HungryHorse'
    return render(request,'HungryHorse1.html',{'hotel':hotel})
  
def final(request):
    a=request.GET['Mutton']
    b=request.GET['Chicken']
    c=request.GET['Paneer']
    f1=items.objects.get(name='Mutton Biryani')
    f2=items.objects.get(name='Chicken Biryani')
    f3=items.objects.get(name='Paneer Fried rice')
    for i in range(int(a)):
        l.append(['Mutton Biryani','price:320.50'])
    for i in range(int(b)):
        l.append(['Chicken Biryani','price:250.50'])
    for i in range(int(c)):
        l.append(['Paneer Fried rice','price:260.50'])
    return render(request,'final.html',{'l':l})
def final1(request):
    subject = 'List of ordered items by the customer'
    message=''
    for i in l:
        message=message+str(i)
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['yellumahanthysaipavan@gmail.com', ]
    send_mail( subject, message, email_from, recipient_list )
    return render(request,'final1.html')
