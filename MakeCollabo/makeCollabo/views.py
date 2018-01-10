from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from .models import Post
# Create your views here.

def index(request):
  return render(request, 'index.html', {})

def about(request):
  return render(request, 'about.html', {})

def viewmore(request):
  posts = Post.objects.all()
  return render(request, 'viewmore.html', {'posts' : posts})

@login_required
def addpost(request):
  if request.method == 'POST':
    form = PostForm(request.POST)
    if form.is_valid():
      post = form.save(commit=False)
      post.author = request.user
      post.save()
      return redirect('viewmore')
  else:
    form = PostForm()
    return render(request, 'addpost.html', {'form' : form})

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