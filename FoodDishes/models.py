from django.db import models

# Create your models here.

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=25)
    items = models.JSONField()
    lat_long = models.CharField(max_length=60)
    full_details = models.JSONField(null=True,blank=True)

    def __str__(self):
        return str(self.name)