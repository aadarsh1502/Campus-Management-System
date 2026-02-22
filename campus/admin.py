from django.contrib import admin
from .models import CampusBlock, Classroom, Course, Faculty, Student

admin.site.register(CampusBlock)
admin.site.register(Classroom)
admin.site.register(Course)
admin.site.register(Faculty)
admin.site.register(Student)