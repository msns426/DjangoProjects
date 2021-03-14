from django.contrib import admin
from .models import Employee,EmployeeDetails,Department
# Register your models here.

admin.site.register([Employee,EmployeeDetails,Department])