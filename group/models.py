from django.db import models

# Create your models here.
from django.contrib.auth.models import User
# Create your models here.
class About(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    major = models.CharField(max_length=300)
    about = models.TextField()
    linkedin = models.CharField(max_length=200)
    instagram = models.CharField(max_length=200)
    github = models.CharField(max_length=300)
    gmail = models.EmailField()
    picture = models.ImageField(upload_to="media/")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"