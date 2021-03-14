from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee
# Create your views here.


def helo(request):
    emp=Employee.objects.all()
    return render(request,'Home.html',{"emp":emp})

