from django.db import models


class List(models.Model):
    title = models.CharField(max_length=255)


class Ticket(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    state = models.BooleanField()
    list = models.ForeignKey(List)