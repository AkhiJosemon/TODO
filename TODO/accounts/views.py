from django.shortcuts import render,redirect
from django.views import View
from .forms import SignUpForm,LoginForm
from django.contrib import messages
from .models import Account
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login ,logout


class SignUpView(View):
    def get(self, request):
        if  request.user.is_authenticated:
            return redirect('base:home')
        form = SignUpForm()
        return render(request, 'User/signup.html', {'form': form})
    
    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            # Extract cleaned data from the form
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data.get('password')
            confirm_password = form.cleaned_data.get('confirm_password')

            if confirm_password != password:
                messages.error(request, "Passwords do not match.")
                return render(request, 'User/signup.html', {'form': form})
            
            # Create a new instance of the Account modelusername , email, first_name, last_name
            user = Account.objects.create_user(username=email, email=email,  first_name=first_name, last_name=last_name,password=password)
            
            
            messages.success(request, "User created successfully.")
            return redirect('accounts:login')   # Redirect to home page after successful sign-up
        
        messages.error(request, "Form submission failed. Please check the form and try again.")
        return render(request, 'User/signup.html', {'form': form})
    

class LoginView(View):
    def get(self,request):
        if  request.user.is_authenticated:
            return redirect('base:home')
        form = LoginForm()
        return render(request,'User/login.html',{'form':form})
    
   
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
           
            
            # Authenticate user
            user = authenticate(username=username,password=password)
            print(user)
            if user is not None:
                # User authentication successful, log the user in
                login(request, user)
                return redirect('base:todo')  # Redirect to home page after successful login
            else:
                # User authentication failed
                form.add_error('username', "Invalid username or password.")
        
        # If form is invalid or authentication fails, render the login page with errors
        return render(request, 'User/login.html', {'form': form})

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('base:home')  # Redirect to the home page after logout