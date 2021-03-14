from django.contrib import admin
from .models import Student,Exam_Details
# Register your models here.
admin.site.register([Student,Exam_Details])