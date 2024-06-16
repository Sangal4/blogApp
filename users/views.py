from django.shortcuts import render,redirect
from .user import userRegisterForm,userUpdationForm,profileUpdationForm
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method=='POST':
      form=userRegisterForm(request.POST)
      if form.is_valid():
         form.save()
         username=form.cleaned_data.get('username')
         messages.success(request,f"your account has been successfully created.you may login now!")
         return redirect('login')
    else:
      form=userRegisterForm()
    return render(request,"users/register.html",{"form":form})


@login_required(login_url='login')  
def profile(request):
  if request.method=='POST':    
    u_form=userUpdationForm(request.POST,instance=request.user)
    p_form=profileUpdationForm(request.POST,request.FILES,instance=request.user.profile)
    if u_form.is_valid() and p_form.is_valid():
          u_form.save()
          p_form.save()
          messages.success(request,f"your profile has been successfully updated")
          return redirect('profile')
  else: 
    u_form=userUpdationForm(instance=request.user)
    p_form=profileUpdationForm(instance=request.user.profile)
        
  context={
    'u_form':u_form,
    'p_form':p_form,
  }
  return render(request,'users/profile.html',context)
  



def logout_page(request):
  logout(request)
  return render(request,'users/logout.html')