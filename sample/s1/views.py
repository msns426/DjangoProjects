from django.shortcuts import render
from django.http import HttpResponse


def display(request):
    return HttpResponse("<h1>Hello this is my first app</h1>")


