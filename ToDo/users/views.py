from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from .forms import UserRegisterForm, ProfileUpdateForm, CreatePost
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin

def register(request):
    if request.method=="POST":
        form = UserRegisterForm(request.POST)
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})

@login_required
def profile(request):
    if request.method == "POST":
        form = ProfileUpdateForm(data = request.POST, instance=request.user)
        if form.is_valid():
            form.save()
    else:
        form = ProfileUpdateForm()
    return render(request, "users/profile.html", {'form':form})

def todo(request):
    posts = Post.objects.filter(author = request.user)
    context = {
        'posts':posts
    }
    return render(request, "users/todolist.html", context)

def delete(request, tid):
    print(Post.objects.all())
    obj = Post.objects.get(id = tid)
    obj.delete()
    return redirect('todo')

@login_required
def create(request):
    if request.method == "POST":
        form = CreatePost(request.POST)
        print(request.user, form.data)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('todo')
        else:
            print('nahi hua solve issue')
    else:
        form = CreatePost()
    return render(request, "users/post_form.html", {'form':form})

