from django.shortcuts import render
from rest_framework import viewsets

from .serializers import EmployeeSerializer
from .models import Employee


class EmpViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all().order_by('ename')
    serializer_class = EmployeeSerializer
