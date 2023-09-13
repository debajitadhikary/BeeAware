from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.models import User , auth
from django.contrib import messages
from .models import Feature

# Create your views here.
def index(request):
    features = Feature.objects.all()
    return render(request,'index.html', {'features':features})
    # return HttpResponse('<h1> Het , Welcome<h1>')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already used')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username , email=email , password=password)
                user.save();
                return redirect('login')
        else:
            messages.info(request, 'Password not same')
            return redirect('register')
    else:
        return render(request , 'register.html')

