from django.shortcuts import render, redirect

from accounts.forms import RegistrationForm
from django.contrib.auth import login, authenticate, logout

def register(request):
      if (request.method == 'POST'):
          form = RegistrationForm(request.POST)
          print(form.is_valid(), 'validity')
          if (form.is_valid()):
              user = form.save()
              print(user, 'user')
              login(request, user)
              return redirect('/')
          
      else:
          form = RegistrationForm()
      return render(request, 'registration/register.html', {'form': form})
  
def login_view(request):
    
    nextUrl = request.GET.get('next', '/')
    if (request.method == 'POST'):
        
        username = request.POST['username']
        password= request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        print(user, 'user')
        if user is not None:
           login(request, user)
           return redirect(nextUrl)
        
    return render(request, 'registration/login.html')

def logout_view(request):
    logout(request)
    return redirect('/accounts/login')