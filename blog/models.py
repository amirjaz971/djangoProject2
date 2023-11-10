from django.db import models
from accounts.models import UserProfile
# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=200)
    body=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.body},{self.title}'

class Comment(models.Model):
    author=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    post=models.ForeignKey(Post, on_delete=models.CASCADE) #Has-A relation-ship
    body=models.TextField()
    is_validate=models.BooleanField()
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)    
    def __str__(self):
        return f'{self.body}'