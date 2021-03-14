from django.db import models

# Create your models here.


class Employee(models.Model):
    emp_id = models.IntegerField(max_length=5,primary_key=True)
    emp_name = models.CharField(max_length=30)
    department=models.ForeignKey("Department",on_delete=models.CASCADE)


class Department(models.Model):
    dept_name=models.CharField(max_length=30)
    manager=models.CharField(max_length=20)
    hr=models.CharField(max_length=20)


class EmployeeDetails(models.Model):
    employee=models.OneToOneField(Employee)
    join_date=models.DateField()
    emp_salary=models.FloatField(max_length=10)
    emp_leave=models.DateField()

