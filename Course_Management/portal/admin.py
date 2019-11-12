from django.contrib import admin

from .models import *


class ClassroomAdmin(admin.ModelAdmin):
    model = Classroom
    list_display = ['Building', 'RoomNo', 'Capacity']
    list_filter = ['Building']


class CourseAdmin(admin.ModelAdmin):
    model = Course
    list_display = ['CourseID', 'CourseName', 'dept_name', 'Credits']
    list_filter = ['DeptName']

    @staticmethod
    def dept_name(obj):
        return f'{obj.DeptName.DeptName}'


class DepartmentAdmin(admin.ModelAdmin):
    model = Department
    list_display = ['DeptName']


class PrerequisiteAdmin(admin.ModelAdmin):
    model = Prerequisites
    list_display = ['course_name', 'prereq_name']

    @staticmethod
    def course_name(obj):
        return f'{obj.CourseID.CourseID} ({obj.CourseID.CourseName})'

    @staticmethod
    def prereq_name(obj):
        return f'{obj.PrereqID.CourseID} ({obj.PrereqID.CourseName})'


class QuestionPaperAdmin(admin.ModelAdmin):
    model = QuestionPaper
    list_display = ['course_id', 'ExamName', 'Semester', 'Year']
    list_filter = ['CourseID']

    @staticmethod
    def course_id(obj):
        return f'{obj.CourseID.CourseID}'


class ProjectAdmin(admin.ModelAdmin):
    model = Project
    list_display = ['ProjectID', 'Title', 'InstID']
    list_filter = ['InstID']


class TakesProjectAdmin(admin.ModelAdmin):
    model = TakesProject
    list_display = ['project_name', 'Student']

    @staticmethod
    def project_name(obj):
        return f'{obj.Project.Title}'


class SectionAdmin(admin.ModelAdmin):
    model = Section
    list_display = ['SecID', 'course_id', 'Semester', 'Year', 'Classroom']
    list_filter = ['CourseID']

    @staticmethod
    def course_id(obj):
        return f'{obj.CourseID.CourseID}'


class TakesAdmin(admin.ModelAdmin):
    model = Takes
    list_display = ['Student', 'Section', 'Grade']
    list_filter = ['Student']


class TeachesAdmin(admin.ModelAdmin):
    model = Teaches
    list_display = ['InstID', 'Section']
    list_filter = ['InstID']


class SpecializationAdmin(admin.ModelAdmin):
    model = Specialization
    list_display = ['Spec']


class SurveyAdmin(admin.ModelAdmin):
    model = Survey
    list_display = ['Student', 'Spec', 'course_id']
    list_filter = ['Spec']

    @staticmethod
    def course_id(obj):
        return f'{obj.Course.CourseID}'


admin.site.register(Course, CourseAdmin),
admin.site.register(Prerequisites, PrerequisiteAdmin)
admin.site.register(QuestionPaper, QuestionPaperAdmin)
admin.site.register(Classroom, ClassroomAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(TakesProject, TakesProjectAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Takes, TakesAdmin)
admin.site.register(Teaches, TeachesAdmin)
admin.site.register(Specialization, SpecializationAdmin)
admin.site.register(Survey, SurveyAdmin)
