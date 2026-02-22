from django.db import models
from django.contrib.auth.models import User

class CampusBlock(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Classroom(models.Model):
    block = models.ForeignKey(CampusBlock, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} - {self.block.name}"

class Course(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    credits = models.IntegerField()
    block = models.ForeignKey(CampusBlock, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return f"{self.code} - {self.name}"

class Faculty(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    courses = models.ManyToManyField(Course, blank=True)

    def __str__(self):
        return self.user.get_full_name()

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roll_no = models.CharField(max_length=20)
    courses = models.ManyToManyField(Course, blank=True)

    def __str__(self):
        return f"{self.roll_no} - {self.user.get_full_name()}"