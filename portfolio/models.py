from django.db import models
from team.models import Team
from blogs.models import Category


# Create your models here.

class Portfolio(models.Model):
    agent = models.ForeignKey(Team,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    desc1 = models.TextField()
    desc2 = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    img1 = models.ImageField(upload_to='portfolio', default='default.png')
    img2 = models.ImageField(upload_to='portfolio', default='default.png')
    img3 = models.ImageField(upload_to='portfolio', default='default.png')
    project_url = models.CharField(max_length=70)
    client = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)


    def __str__(self):
        return self.title