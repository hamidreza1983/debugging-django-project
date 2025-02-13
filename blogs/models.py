from django.db import models
from team.models import Team

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=50)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Tag(models.Model):
    title = models.CharField(max_length=50)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Blog(models.Model):
    agent = models.ForeignKey(Team,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    desc1 = models.TextField()
    desc2 = models.TextField()
    desc3 = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)
    img1 = models.ImageField(upload_to='blog', default='default.png')
    img2 = models.ImageField(upload_to='blog', default='default.png')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    def truncate_chars(self):
        return self.desc1[:20]
    
    class Meta:
        ordering = ["-created_at"]



class Comments(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    message = models.TextField()
    post = models.CharField(max_length=50)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.blog.title
    

class Reply(models.Model):
    comment = models.ForeignKey(Comments, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    message = models.TextField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.comment.blog.title




