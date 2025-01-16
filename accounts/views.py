from django.shortcuts import render, redirect

from accounts.forms import RegistrationForm
from django.contrib.auth import login, authenticate

def register(request):
      if (request.method == 'POST'):
          form = RegistrationForm(request.POST)
          
          if (form.is_valid()):
              user = form.save()
              login(request, user)
              return redirect('/')
          
      else:
          form = RegistrationForm()
      return render(request, 'registration/register.html', {'form': form})