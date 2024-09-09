from django.shortcuts import render, redirect, reverse
from .models import *
# Create your views here.

def Registerpage(request):
    return render(request,'app/register.html')


def UserRegister(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        contact = request.POST['contact']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        exist_user = Registeruser.objects.filter(Email=email)
        
        if exist_user:
            message = 'User alreday Exists'
            return render(request,'app/register.html',{'msg':message})
        
        else:
            if password == cpassword:
                new_user = Registeruser.objects.create(Firstname=fname,Lastname=lname,
                                        Email=email,Contact=contact,Password=password)
                message = 'User register Succcessfully'
                return render(request,'app/login.html',{'msg':message})
            
            else:
                message = 'Password doesnot match with Confirm Password'
                return render(request,'app/register.html',{'msg':message}) 

def Loginpage(request):
    return render(request,'app/login.html')


def UserLogin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            user_mail = Registeruser.objects.get(Email=email)
            if user_mail.Password == password:
                request.session['Firstname'] = user_mail.Firstname
                request.session['Lastname'] = user_mail.Lastname
                request.session['Email'] = user_mail.Email
                return render(request, 'app/home.html')
            else:
                message = 'Password does not match'
                return redirect(reverse('loginpage'), {'message': message})  # Redirect with error message using reverse lookup
        except Registeruser.DoesNotExist:
            message = 'User does not Exist'
            return redirect(reverse('loginpage'), {'message': message})  # Redirect with error message using reverse lookup
