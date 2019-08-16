from django.db import models

class SkypeData(models.Model):
    #login = models.CharField(max_length=255)
    #password = models.CharField(max_length=255)
    chatName = models.CharField(max_length=255,default="Learning is an awesome journey")

class Links(models.Model):
    link = models.CharField(max_length=255)