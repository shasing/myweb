from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render,HttpResponse 

# Create your views here.
def home(request):
        return HttpResponse("welcome")
def abc(request):
        return HttpResponse("hello")

def indexs(request):
        return render(request, 'index.html') 

def gmail(request):
    send_mail(
    'Subject here',
    'Here is the message.',
    'shalinisingh199605@gmail.com',
    ['shalinisingh199605@gmail.com'],
    fail_silently=False,)
    return render(request, 'gmail.html') 

def base(request):
        return render(request, 'base.html')
def new_user(request):
        return render(request, 'new_user.html')
def login(request):
        return render(request, 'login.html')
def relogin(request):
        return render(request, 'home.html')


#subject = 'hey there'
        #message = 'ir'
        #email_from = 'shalinisingh199605@gmail.com'
        #recipient_list = ['shalinisingh199605@gmail.com']
    
    #return redirect('index.html')


"""
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from yourapp.forms import ContactForm

def email(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('index')
    return render(request, "email.html", {'form': form})

def thanks(request):
    return HttpResponse('Thank you for your message.')"""
