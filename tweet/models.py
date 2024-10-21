from django.db import models

#importing the User from admin panel , this will used to create model and store the data#
from django.contrib.auth.models import User;

# Create your models here.
#here we are associating every tweet with user#
class Tweet(models.Model):
    
    user = models.ForeignKey(User,on_delete=models.CASCADE);

    text = models.TextField(max_length=240)

    photo = models.ImageField(upload_to="photos/",blank=True,null=True); 



