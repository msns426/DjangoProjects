from django.db import models

# Create your models here.


class Student(models.Model):
    sno=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Exam_Details(models.Model):
    student=models.OneToOneField(Student,on_delete=models.CASCADE)
    city=models.CharField(max_length=15)
    hallticket = models.IntegerField(max_length=10,default=True)

    def __str__(self):
        return self.student.name + "(" + self.city +")"


