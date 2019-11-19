from django import forms
from django.contrib.auth.models import User
from django.db import models
from .models import *

class FeedbackForm(forms.ModelForm):
	class Meta:
		model = Feedback
		fields = ['CourseID', 'Feedback',]


class CourseRegisterForm(forms.ModelForm):
    class Meta:
        model = TakesCourse
        fields = ['Course', 'CourseID', 'Student', 'Year', 'Sem']
    def __init__(self, *args, **kwargs):
        super(CourseRegisterForm, self).__init__(*args, **kwargs)
        self.fields['CourseID'].required = False
        self.fields['Student'].required = False