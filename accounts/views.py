from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from accounts.forms import RegistrationForm
from django.contrib.auth import login, authenticate, logout

def register(request):
      error = None
      if (request.method == 'POST'):

          try:
            username = request.POST['username']
            email = request.POST['email']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            
            if password1 != password2:
                return render(request, 'registration/register.html', {'error': 'Passwords do not match'})
            
            user = User.objects.create(
                username=username,
                email=email,
                password=password1
                
            )

            login(request, user)
            return redirect('/')
            
          except Exception as e:
            error = e
          
      
      return render(request, 'registration/register.html', {'error': error,})
  
def login_view(request):
    
    if (request.method == 'POST'):
        
        username = request.POST['username']
        password= request.POST['password']
        
        user = authenticate(username=username, password=password)
        
        print(user, 'user')
        if user is not None:
           login(request, user)
           return redirect('/')
        
    return render(request, 'registration/login.html')

def logout_view(request):
    logout(request)
    return redirect('/accounts/login')