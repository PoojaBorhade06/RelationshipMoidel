from django.contrib import admin
from .models import Student,Department,Lecturer
# Register your models here.

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['dept_name', 'dept_seats']

admin.site.register(Department,DepartmentAdmin)

class StudentAdmin(admin.ModelAdmin):
    list_display = ['stu_rn', 'stu_name', 'stu_marks']
admin.site.register(Student,StudentAdmin)


class LecturerAdmin(admin.ModelAdmin):
    list_display = ['name', 'salary']
admin.site.register(Lecturer,LecturerAdmin)