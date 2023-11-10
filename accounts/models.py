from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
# Create your models here.
class UserProfile(models.Model):
    bio=models.CharField(max_length=50)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    picture=models.ImageField(upload_to='profile_picture',default='default_profile_picture.png') #pip install pillow


class Edjucation(models.Model):
    school=models.CharField(max_length=50)
    degree=models.CharField(max_length=50)
    field=models.CharField(max_length=50)
    start=models.DateTimeField()
    end=models.DateTimeField()
    desc=models.TextField()

class Experience(models.Model):
    title=models.CharField(max_length=50)
    company=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    start=models.DateTimeField()
    end=models.DateTimeField()
    desc=models.TextField()

@receiver(post_save,sender=User,dispatch_uid="create_user_profile")  
def create_userprofile(sender,instance, **kwargs):
    if UserProfile.objects.filter(user=instance).count()==0:
        UserProfile.objects.create(user=instance)
   
#sqlite3 db.sqlite3 .database env values add path c:\sqlite