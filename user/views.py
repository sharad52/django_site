from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages


# Create your views here.


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('django_app:home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request,'Accounts was created for ' + user)
                return redirect('userAuth:login')

        context = {'form':form}

        return render(request,'register.html',context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('django_app:home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username,password=password)

            if user is not None:
                login(request,user)
                return redirect('django_app:home')

            else:
                messages.info(request,"Username OR password is incorrect ")
                return render(request,'login.html')

        context = {}

        return render(request,'login.html',context)


def logoutUser(request):
    logout(request)

    return redirect('userAuth:login')
