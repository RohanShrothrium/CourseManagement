from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Course(models.Model):
    CourseID = models.CharField(max_length=5)
    CourseName = models.TextField()
    DeptName = models.TextField()
    Credits = models.IntegerField()
    Feedback = models.TextField()

    def __str__(self):
        return self.CourseID


class Classroom(models.Model):
    Building = models.CharField(max_length=25, default='')
    RoomNo = models.CharField(max_length=5, default='')
    Capacity = models.IntegerField(default=0)


class Instructor(models.Model):
    InstID = models.CharField(max_length=5, default='')
    InstName = models.TextField(default='')
    DeptName = models.TextField(default='')
    Email = models.EmailField()


class Project(models.Model):
    ProjectID = models.CharField(max_length=5, default='')
    InstID = models.CharField(max_length=5, default='')
    Title = models.TextField()
    Description = models.TextField()


class TakesProject(models.Model):
    Project = models.ForeignKey(Project, on_delete=models.CASCADE)
    Student = models.ForeignKey(User, on_delete = models.CASCADE)
    Performance = models.TextField()
    Feedback = models.TextField()
