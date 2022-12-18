from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

class CustomUser(AbstractUser):
    user = (
        (1,'Admin'),
        (2,'Teacher'),
        (3,'Student'),
    )
    user_type = models.CharField(choices=user,max_length=50,default=3)
    # profile_pic = models.ImageField(upload_to='media/profile_pic')

class Admin(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    # username = models.CharField(max_length=100)
    # first_name = models.CharField(max_length=100)
    # last_name = models.CharField(max_length=100)
    # email = models.CharField(max_length=100)
    # password = models.CharField(max_length=300)
    address = models.TextField()


    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    object = models.Manager()  

class Teacher(models.Model):
    id = models.AutoField(primary_key=True)
    teacher = models.OneToOneField(CustomUser,on_delete=models.CASCADE)

    # username = models.CharField(max_length=100)
    # first_name = models.CharField(max_length=100)
    # last_name = models.CharField(max_length=100)
    # email = models.CharField(max_length=100)
    # password = models.CharField(max_length=300)
    class_teacher = models.CharField(max_length=100)


    address = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    object = models.Manager()

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.OneToOneField(CustomUser,on_delete=models.CASCADE)

    class_teacher = models.ForeignKey(Teacher,on_delete=models.DO_NOTHING,null=True,blank=True)
    # username = models.CharField(max_length=100)
    # first_name = models.CharField(max_length=100)
    # last_name = models.CharField(max_length=100)
    # email = models.CharField(max_length=100)
    roll = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    guardian = models.CharField(max_length=100)
    guardian_phone_number = models.CharField(max_length=100)
    grade = models.CharField(max_length=100)
    section = models.CharField(max_length=100)
    faculty = models.CharField(max_length=100)
    object = models.Manager()

    

    
    password = models.CharField(max_length=300)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    


@receiver(post_save,sender=CustomUser)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        if instance.user_type==1:
            Admin.object.create(admin=instance)
        if instance.user_type==2:
            Teacher.object.create(teacher=instance)
        if instance.user_type==3:
            Student.object.create(student=instance)
        
@receiver(post_save,sender=CustomUser)
def save_user_profile(sender,instance,**kwargs):

        if instance.user_type==1:
            instance.admin.save()
        if instance.user_type==2:
            instance.teacher.save()
        if instance.user_type==3:
            instance.student.save()
        
        
