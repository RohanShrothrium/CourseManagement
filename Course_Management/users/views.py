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


def register(request):
    if request.method == 'POST':
        form = CourseRegisterForm(request.POST)
        if form.is_valid():
            for i in request.user.takescourse_set.all():
                if i.CourseID == form.instance.Course.CourseID:
                    messages.warning(request, f'You have already taken up {i.CourseID} !')
                    return redirect('profile')
            for i in Prereqs.objects.all():
                if i.CourseID == form.instance.Course.CourseID:
                    temp = 0
                    for j in request.user.takescourse_set.all():
                        if i.PrereqID == j.CourseID:
                            temp = 1
                    if not temp:
                        messages.warning(request, f'You have not finished the prerequisites for {i.CourseID} !')
                        return redirect('profile')
            form.instance.Student = request.user
            form.instance.CourseID = form.instance.Course.CourseID
            form.save()
            return redirect('profile')
    else:		
        # we come here first and.....
        form = CourseRegisterForm()
        form.instance.Student = request.user
    context = {
        'courses': Course.objects.all(),
        'form': form
    }
    return render(request, 'users/register.html', context)


def projects(request):
    context = {
        'projects': request.user.takesproject_set.all(),
        'courses': request.user.takescourse_set.all()
    }
    return render(request, 'users/projects.html', context)


def prevcourses(request):
    context = {
        'courses': request.user.takescourse_set.all()
    }
    return render(request, 'users/prevcourses.html', context)


def Question_Paper(request, Course_ID):
    context = {
        'Course' : Course.objects.all().filter(CourseID=Course_ID).first(),
        'QuestionPaper': QuestionPaper.objects.all().filter(CourseID=Course_ID)
    }
    return render(request, 'users/questionpapers.html', context)