from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import *
from .models import *
from portal.models import QuestionPaper

# Create your views here.
@login_required
def profile(request):
    context = {
        'projects': request.user.takesproject_set.all(),
        'courses': request.user.takescourse_set.all()
    }
    return render(request, 'users/profile.html', context)


def courses(request):
    if request.method == 'POST':
        # here next...
        form = FeedbackForm(request.POST)
        if form.is_valid():
            print(form.instance.CourseID)
            temp = request.user.takescourse_set.all().filter(CourseID=form.instance.CourseID).first()
            temp.FeedbackGiven = 1
            temp.save()
            form.save()
            return redirect('profile')
    else:		
        # we come here first and.....
        form = FeedbackForm()
    context = {
        'courses': request.user.takescourse_set.all(),
        'form': form
    }
    return render(request, 'users/courses.html', context)


def projects(request):
    context = {
        'projects': request.user.takesproject_set.all(),
        'courses': request.user.takescourse_set.all()
    }
    return render(request, 'users/projects.html', context)


def Question_Paper(request, Course_ID):
    context = {
        'QuestionPaper': QuestionPaper.objects.all().filter(CourseID=Course_ID[1:6])
    }
    return render(request, 'users/questionpapers.html', context)