from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return  render(request,"home.html",{"name":"satya"})


def add(request):
    a=int(request.POST["FN"])
    b=int(request.POST["SN"])
    res=a+b
    return render(request,"result.html",{"result":res})