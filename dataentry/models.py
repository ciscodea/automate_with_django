from django.db import models


class Student(models.Model):
    roll_no = models.CharField(max_length=255)
    name = models.CharField(max_length=20)
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=20)
    country = models.CharField(max_length=20)

    def __str__(self):
        return self.name
