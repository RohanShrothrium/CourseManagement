from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
@login_required
def profile(request):
    context = {
        'projects': request.user.takesproject_set.all()
    }
    return render(request, 'users/profile.html', context)