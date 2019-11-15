from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
@login_required
def profile(request):
    context = {
        'projects': request.user.takesproject_set.all(),
        'courses': request.user.takescourse_set.all()
    }
    return render(request, 'users/profile.html', context)


def courses(request):
    context = {
        'courses': request.user.takescourse_set.all()
    }
    return render(request, 'users/courses.html', context)


def projects(request):
    context = {
        'projects': request.user.takesproject_set.all(),
        'courses': request.user.takescourse_set.all()
    }
    return render(request, 'users/projects.html', context)