from django.db import models

# Create your models here.


class Employee(models.Model):
    eno=models.IntegerField(primary_key=True,auto_created=True)
    ename=models.CharField(max_length=20)
    esal=models.FloatField()
    eemail=models.EmailField(max_length=50,unique=True)

    def __str__(self):
        return self.ename


class Department(models.Model):
    employee=models.OneToOneField(Employee,on_delete=models.CASCADE,primary_key=True)
    city=models.CharField(max_length=20,default=False)
    dept_name=models.CharField(max_length=30,default=False)

    def __str__(self):
        return self.employee.ename

