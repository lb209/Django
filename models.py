from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=50)
    city = models.CharField(max_length=100)
    age=models.IntegerField()
   
class Image(models.Model):
    image=models.ImageField(upload_to="uploads/")


def __str__(self):
   return self.name
