from django.db import models
from django.db.models.fields import DateTimeField, CharField, TextField
from django.shortcuts import render

class Blog(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    body = models.TextField(max_length=500)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

        return super().__str__()
    def summary(self):
        return self.body[:100]
    
    def pub_date_pretty(self):
        return self.pub_date.strftime('%d %B, %Y')