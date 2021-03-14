from django.db import models

# Create your models here.


class Album(models.Model):
    name=models.CharField(max_length=30)
    artist=models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Songs(models.Model):
    title=models.CharField(max_length=20)
    album=models.ForeignKey(Album,on_delete=models.CASCADE)

    def __str__(self):
        return self.title


