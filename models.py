from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.IntegerField(max_length=111)
    course = models.CharField(max_length=100)
    image = models.ImageField(upload_to="students/", blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.roll_number} - {self.course}"


class Teacher(models.Model):
    name = models.CharField(max_length=20)
    sub = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name} - {self.sub}"