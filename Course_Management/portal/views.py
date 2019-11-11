from django.shortcuts import render

from .models import *


# Create your views here.
def home(request):
    context = {
        'courses': Course.objects.all()
    }
    return render(request, 'portal/home.html', context)


def about(request):
    return render(request, 'portal/about.html')
