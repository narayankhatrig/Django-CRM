from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserInformation


# Create your views here.

def home(request):

    #get all objects from UserInformation model
    userInfo = UserInformation.objects.all()

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        #authenticate the user
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, "You Have Been Logged In!")
            return redirect('home')
        else:
            messages.success(request, "There Was An Error Login In ! Please Try Again...")
            return redirect('home')
    else:
        return render(request, 'home.html', {'userInfo':userInfo})


'''def login_user(request):
    return render(request, 'home.html')
'''

@login_required(login_url='home')
def logout_user(request):
    auth.logout(request)
    messages.success(request, "You Have Been Logged Out!")
    return redirect('home')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.success(request, "Email Already Taken")
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.success(request, "Username Already Taken")
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, password=password, email=email)
                auth.login(request, user)
                messages.success(request, "You Have Successfully Registered...")
                return redirect('home')
        else:
            messages.success(request, "Password Do Not Match!")
    else:
        return render(request, 'signup.html')
    
#function to get user information from database
def getUserInformation(request, pk):
    if request.user.is_authenticated:
        userInfo = UserInformation.objects.get(id=pk)
        return render(request, 'user.html', {'userInfo': userInfo})
    else:
        messages.success(request, "You must be logged in...")
        return redirect('home')
    

#function to delete a record
def deleteUserInformation(request, pk):
    if request.user.is_authenticated:
        userInfo = UserInformation.objects.get(id=pk)
        userInfo.delete()#deletes the record
        messages.success(request, "The user information is deleted !")
        return redirect('home')
    else:
        messages.success(request, "You must be logged in to delete user information")
        return redirect('home')