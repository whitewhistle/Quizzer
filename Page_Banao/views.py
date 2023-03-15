import json
from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from Quizzers import settings
from django.core.mail import send_mail

# Create your views here.


def home(request):
    return render(request, "Page_Banao/index.html")


def signup(request):
    if request.method == "POST":
        
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=username):
            messages.error(request, "Username already exist!")
            return redirect('#modal2')

        if pass1 != pass2:
            messages.error(
                request, "either password or confirm password were typed wrong!")
            return redirect('#modal2')

        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric! ")
            return redirect('#modal2')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname


        messages.success(request, "YOUR ACCOUNT HAS BEEN SUCCESSFULLY CREATED")

        # Welcome Email
        subject = "Welcome to Quizzers!"
        message = "Hello" + myuser.first_name + "!!"
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject, message, from_email, to_list, fail_silently=True)

        return redirect('home')

    return render(request, "Page_Banao/index.html")


def user_login(request):

    if request.method == "POST":

        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, "Page_Banao/index.html", {'fname': fname})

        else:
            messages.error(request, "EITHER WRONG USERNAME OR PASSWORD")
            return redirect('#modal')

    return render(request, "Page_Banao/index.html")


def signout(request):
    logout(request)
    messages.success(request, "LOGOUT SUCESSFULLY")
    return redirect('home')

def createQuiz(request):
    if request.method == 'POST':
      print("hello")
      return render(request, "createQuiz.html")