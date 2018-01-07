from django.shortcuts import render, redirect
from django.contrib.auth.models import User

# Create your views here.

def index(request):
  return render(request, 'index.html', {})

# Show sign up page

def signup(request):
  if request.method == 'POST':
    username = request.POST['username']
    email = request.POST['email']
    pw = request.POST['pw']
    rpw = request.POST['rpw']

    if pw == rpw:
      print(username)
      try:
        user = User.objects.get(username = username)
      except User.DoesNotExist:
        user = User.objects.create_user(username=username, email=email, password=pw)
        user.save()
        return redirect('/accounts/login')

    return render(request, 'registration/signup.html', {})
  else:
    return render(request, 'registration/signup.html', {})