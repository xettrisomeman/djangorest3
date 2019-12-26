from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    pass


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    


class Book(models.Model):
    author = models.ManyToManyField(Author)
    title = models.CharField(max_length=50)
    year = models.IntegerField()

    def __str__(self):
        return self.title



    
