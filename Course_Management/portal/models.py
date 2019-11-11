from django.contrib.auth.models import User
from django.db import models
from users.models import User


class Department(models.Model):
    DeptName = models.CharField(max_length=20, primary_key=True)


class Course(models.Model):
    CourseID = models.CharField(max_length=5, primary_key=True)
    CourseName = models.TextField()
    DeptName = models.ForeignKey(Department, models.SET_NULL, null=True)
    Credits = models.IntegerField()
    Performance = models.CharField(max_length=10, null=True, blank=True)
    Feedback = models.TextField()


class Prerequisites(models.Model):
    CourseID = models.ForeignKey(Course, models.CASCADE, related_name='Course1')
    PrereqID = models.ForeignKey(Course, models.CASCADE, related_name='Course2')

    class Meta:
        unique_together = (('CourseID', 'PrereqID'),)


class QuestionPaper(models.Model):
    CourseID = models.ForeignKey(Course, models.CASCADE)
    ExamName = models.CharField(max_length=30)
    Semester = models.CharField(max_length=10)
    Year = models.IntegerField()
    Path = models.URLField()

    class Meta:
        unique_together = (('CourseID', 'ExamName', 'Semester', 'Year'),)


class Classroom(models.Model):
    Building = models.CharField(max_length=25, default='')
    RoomNo = models.CharField(max_length=5, default='')
    Capacity = models.IntegerField(default=0)

    class Meta:
        unique_together = (('Building', 'RoomNo'),)

    def __str__(self):
        return "%s_%s" % (self.Building, self.RoomNo)


class Instructor(models.Model):
    InstID = models.CharField(max_length=5, default='', primary_key=True)
    InstName = models.TextField(default='')
    DeptName = models.ForeignKey(Department, models.SET_NULL, null=True)
    Email = models.EmailField()


class Project(models.Model):
    ProjectID = models.CharField(max_length=5, default='', primary_key=True)
    InstID = models.CharField(max_length=5, default='')
    Title = models.TextField()
    Description = models.TextField()


class TakesProject(models.Model):
    Project = models.ForeignKey(Project, on_delete=models.CASCADE)
    Student = models.ForeignKey(User, on_delete=models.CASCADE)
    Performance = models.TextField()
    Feedback = models.TextField()

    class Meta:
        unique_together = (('Project', 'Student'),)


class Section(models.Model):
    CourseID = models.ForeignKey(Course, models.SET_NULL, null=True)
    SecID = models.CharField(max_length=20, primary_key=True)
    Semester = models.CharField(max_length=10)
    Year = models.IntegerField()
    Classroom = models.ForeignKey(Classroom, models.SET_NULL, null=True)


class Takes(models.Model):
    Student = models.ForeignKey(User, models.CASCADE)
    Section = models.ForeignKey(Section, models.CASCADE)
    Feedback = models.TextField(blank=True, null=True)
    Grade = models.DecimalField(max_digits=4, decimal_places=2)

    class Meta:
        unique_together = (('Student', 'Section'),)


class Teaches(models.Model):
    InstID = models.ForeignKey(Instructor, models.CASCADE)
    Section = models.ForeignKey(Section, models.SET_NULL, null=True)

    class Meta:
        unique_together = (('InstID', 'Section'),)


class Specialization(models.Model):
    Spec = models.CharField(max_length=30)


class Survey(models.Model):
    Student = models.ForeignKey(User, models.CASCADE)
    Course = models.ForeignKey(Course, models.CASCADE)
    Spec = models.ForeignKey(Specialization, models.SET_NULL, null=True)

    class Meta:
        unique_together = (('Student', 'Course', 'Spec'),)
