from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Employee
from .serializers import Employeeserializers

# Create your views here.
class emplist(APIView):

    def get(self,request):
        employee=Employee.objects.all()
        serializer=Employeeserializers(employee,many=True)
        return Response(serializer.data)

    def post(self,request):
        pass


