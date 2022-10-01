from django.db import models 

class Contact(models.Model):
       email=models.CharField(max_length=122)
       desc=models.TextField(max_length=250)
