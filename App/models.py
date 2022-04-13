from django.db import models

# Create your models here.

class Clients(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    address = models.TextField(max_length=1000,null=True)
    
    def __str__(self):
        return self.name

   