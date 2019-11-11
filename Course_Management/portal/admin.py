from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(Course)
admin.site.register(Classroom)
admin.site.register(Instructor)
admin.site.register(Project)
admin.site.register(TakesProject)
admin.site.register(Department)
