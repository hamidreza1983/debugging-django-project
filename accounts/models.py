from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=30)
    image = models.ImageField(upload_to="user",default="default.png")
    id_code = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)
