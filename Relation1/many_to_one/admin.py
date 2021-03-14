from django.contrib import admin
from .models import Album,Songs
# Register your models here.

admin.site.register([Album,Songs])

