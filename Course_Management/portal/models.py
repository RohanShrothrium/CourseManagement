from django.contrib.auth.models import User
from django.db import models

from users.models import Profile


class Department(models.Model):
    DeptName = models.CharField(max_length=50, primary_key=True)

    class Meta:
        db_table = 'department'


class Course(models.Model):
    CourseID = models.CharField(max_length=5, primary_key=True)
    CourseName = models.CharField(max_length=50)
    DeptName = models.ForeignKey(Department, models.SET_NULL, null=True)
    Credits = models.IntegerField()
    Performance = models.CharField(max_length=10, null=True, blank=True)
    Feedback = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'course'


class Prerequisites(models.Model):
    CourseID = models.ForeignKey(Course, models.CASCADE, related_name='Course1')
    PrereqID = models.ForeignKey(Course, models.CASCADE, related_name='Course2')

    class Meta:
        db_table = 'prerequisite'
        unique_together = (('CourseID', 'PrereqID'),)


class QuestionPaper(models.Model):
    CourseID = models.ForeignKey(Course, models.CASCADE)
    ExamName = models.CharField(max_length=30)
    Semester = models.CharField(max_length=10)
    Year = models.IntegerField()
    Path = models.URLField()

    class Meta:
        db_table = 'question_paper'
        unique_together = (('CourseID', 'ExamName', 'Semester', 'Year'),)


class Classroom(models.Model):
    Building = models.CharField(max_length=25, default='')
    RoomNo = models.CharField(max_length=5, default='')
    Capacity = models.IntegerField(default=0)

    class Meta:
        db_table = 'classroom'
        unique_together = (('Building', 'RoomNo'),)

    def __str__(self):
        return f'{self.Building} ({self.RoomNo})'


class Project(models.Model):
    ProjectID = models.CharField(max_length=5, default='', primary_key=True)
    InstID = models.ForeignKey(Profile, models.SET_NULL, null=True, limit_choices_to={'UserType': 1})
    Title = models.CharField(max_length=500)
    Description = models.TextField()

    class Meta:
        db_table = 'project'


class TakesProject(models.Model):
    Project = models.ForeignKey(Project, on_delete=models.CASCADE)
    Student = models.ForeignKey(Profile, on_delete=models.CASCADE, limit_choices_to={'UserType': 0})
    Performance = models.CharField(max_length=500, blank=True, null=True)
    Feedback = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'takes_project'
        unique_together = (('Project', 'Student'),)


class Section(models.Model):
    CourseID = models.ForeignKey(Course, models.SET_NULL, null=True)
    SecID = models.CharField(max_length=20, primary_key=True)
    Semester = models.CharField(max_length=10)
    Year = models.IntegerField()
    Classroom = models.ForeignKey(Classroom, models.SET_NULL, null=True)

    class Meta:
        db_table = 'section'

    def __str__(self):
        return f'{self.CourseID.CourseID} ({self.Semester}, {self.Year})'


class Takes(models.Model):
    Student = models.ForeignKey(Profile, models.CASCADE, limit_choices_to={'UserType': 0})
    Section = models.ForeignKey(Section, models.CASCADE)
    Feedback = models.TextField(blank=True, null=True)
    Grade = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)

    class Meta:
        db_table = 'takes'
        unique_together = (('Student', 'Section'),)


class Teaches(models.Model):
    InstID = models.ForeignKey(Profile, models.CASCADE, limit_choices_to={'UserType': 1})
    Section = models.ForeignKey(Section, models.SET_NULL, null=True)

    class Meta:
        db_table = 'teaches'
        unique_together = (('InstID', 'Section'),)


class Specialization(models.Model):
    Spec = models.CharField(max_length=30)

    class Meta:
        db_table = 'specialization'

    def __str__(self):
        return f'{self.Spec}'


class Survey(models.Model):
    Student = models.ForeignKey(Profile, models.CASCADE, limit_choices_to={'UserType': 0})
    Spec = models.ForeignKey(Specialization, models.SET_NULL, null=True)
    Course = models.ForeignKey(Course, models.CASCADE)

    class Meta:
        db_table = 'survey'
        unique_together = (('Student', 'Course', 'Spec'),)
