from django.db import models

# Create your models here.


class Skill(models.Model):
    skill = models.CharField(max_length=30)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.skill
    

class Team(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='team', default='default.png')
    skill = models.ManyToManyField(Skill)
    content = models.TextField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name