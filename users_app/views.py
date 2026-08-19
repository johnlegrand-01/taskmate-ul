from django.shortcuts import render
#from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import CustomRegisterForm
from django.contrib import messages
from django.shortcuts import redirect

# Create your views

def register(request):
    if request.method =="POST":
        register_form = CustomRegisterForm(request.POST)
        if  register_form.is_valid():
            register_form.save()
            messages.success(request,"New user account created. Login to Get started", "Succes")
            #return redirect('todolist')
            return redirect('register')
    else:
        register_form  = CustomRegisterForm()
    return render(request,'register.html',{'register_form': register_form } )
