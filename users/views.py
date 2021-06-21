from django.shortcuts import render
from django.http import request
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from users.forms import  UserRegistration, UserEditForm
from django.contrib import messages

@login_required
def dashboard(request):
    return render(request,"users/dashboard.html")

def register(request):
    if request.method == 'POST':
        form=UserRegistration(request.POST)
        if form.is_valid() :
            new_user=form.save(commit=False)
            password = form.cleaned_data['password1']
            new_user.set_password(password)
            new_user.save()
            messages.success(request, 'Account was created for ' , new_user)
            return render(request,'registration/registration_done.html')


    else:
        form=UserRegistration()
        
    context = {"form": form}
    return render(request,'registration/register.html',context=context) 


@login_required
def edit(request):
    if request.method == 'POST':
        user_form=UserEditForm(instance=request.user,data=request.POST)
        if user_form.is_valid():
            user_form.save()
    else:
        user_form=UserEditForm(instance=request.user)
    context = {'form': user_form}
    return render(request,'users/edit.html',context=context)


