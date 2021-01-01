from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,  logout
from django.contrib.auth import login as loginn
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    print(request.user)
    if request.user.is_authenticated is True:
        return redirect("home/")
    
    return render(request, 'home.html')

def loginhandle(request):

    if request.method == "POST":
        login_username = request.POST.get("username")
        login_pass = request.POST.get("pass")

        user = authenticate(username=login_username, password=login_pass)

        if user is not None:
            if user.is_active:
                loginn(request, user)
                return redirect("/home")

        else:

            return redirect("/")

def signup(request):
    if request.method == "POST":
        print("DOne")
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        print(username, fname, lname, email, pass1, pass2)

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        user = authenticate(username=username, password=pass1)
        loginn(user)
        return redirect('/home')
    else:
        return HttpResponse("404 Not Found")

def logout_handle(request):
    print(request)
    logout(request)

    return redirect("/")