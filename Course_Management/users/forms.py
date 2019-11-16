from django import forms
from django.contrib.auth.models import User
from django.db import models
from .models import *

class FeedbackForm(forms.ModelForm):
	class Meta:
		model = Feedback
		fields = ['CourseID', 'Feedback',]