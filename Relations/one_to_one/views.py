from django.shortcuts import render
from django.views.generic import View
from .models import *

# Create your views here.


def Home(request):
    def get(self, request):
        person=Student.objects.all()
        print(person)
        return render(request,"index.html",{'person':person})
