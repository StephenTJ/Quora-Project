from django.shortcuts import render, redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from . import forms
# Create your views here.
def Login_Page(request):
    if request.method == 'POST':
        form = forms.LoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Login successful." )
                return redirect('questions')
            else:
                return redirect('login')
        else:
            return redirect('login')
    else:
        form = forms.LoginForm()
        return render(request, 'login_page.html',{'form':form})

def Logout_Page(request):
	logout(request)
	# messages.info(request, "You have successfully logged out.") 
	return redirect("login")

def Signup_Page(request):
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Registration successful.")
            return redirect('signup')
        else:
            # Form is not valid, show an error message in the template
            messages.error(request, "Unsuccessful registration. Invalid information.")
            return redirect('signup')
    else:
        form = forms.SignupForm()

    return render(request, 'signup_page.html', {'form': form})