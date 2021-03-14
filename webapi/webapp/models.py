from django.db import models


class Employee(models.Model):
    no=models.IntegerField()
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)

    def __str__(self):
        return  self.fname
