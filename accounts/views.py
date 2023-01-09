from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.

def signup_view(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      # log the user in
      login(request, user)
      return redirect('shows:list')
  else:
    form = UserCreationForm()
  return render(request, 'signup.html', {'form':form})
