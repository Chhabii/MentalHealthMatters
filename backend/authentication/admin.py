from django.contrib import admin
from django.db import models
from .models import CustomUser,Teacher,Student,Admin
from django.contrib.auth.admin import UserAdmin


class UserModel(UserAdmin):
    list_display = ['id','username','user_type']

@admin.register(Admin)
class userAdmin(admin.ModelAdmin):
    list_display = ['id']

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id']

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id']



admin.site.register(CustomUser,UserModel)
# admin.site.register(Teacher)
# admin.site.register(Student)
# admin.site.register(Admin)

