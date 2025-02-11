from django.db import models

# Create your models here.

class Services(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    status = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title