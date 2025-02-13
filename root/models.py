from django.db import models

# Create your models here.



class Testimonials(models.Model):
    title = models.CharField(max_length=20)
    logo = models.ImageField(upload_to='testimonials', default='default.png')
    content = models.TextField()
    domain = models.CharField(max_length=50)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title



class Contactus(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()


    def __str__(self):
        return self.subject

