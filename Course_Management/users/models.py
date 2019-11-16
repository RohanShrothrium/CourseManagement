from django.db import models
from django.contrib.auth.models import User
from portal.models import *

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    DepName = models.CharField(max_length=10, default='')
    Cpi = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    def __str__(self):
        return f'{self.user.username} Profile'



class TakesProject(models.Model):
    Project = models.ForeignKey(Project, on_delete=models.CASCADE)
    Student = models.ForeignKey(User, on_delete = models.CASCADE)
    Performance = models.TextField()
    Feedback = models.TextField()
    def __str__(self):
        return f'{self.Project.ProjectID} Project'


class TakesCourse(models.Model):
    Course = models.ForeignKey(Course, on_delete=models.CASCADE)
    CourseID = models.CharField(max_length=5, default='')
    Student = models.ForeignKey(User, on_delete = models.CASCADE)
    Year = models.CharField(max_length=4)
    Sem = models.CharField(max_length=6)
    Grade = models.CharField(max_length=2, default='OG')
    FeedbackGiven = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    def __str__(self):
        return f'{self.Course.CourseID} Course'
    

class Feedback(models.Model):
    CourseID = models.CharField(max_length=5, default='')
    Feedback = models.TextField()
