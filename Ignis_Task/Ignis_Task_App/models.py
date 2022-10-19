from django.db import models
# Create your models here.

class Events(models.Model):
    event_name = models.CharField(max_length=300,null=False,blank=False)
    location = models.CharField(max_length=300,null=False,blank=False)
    event_date = models.DateField(max_length=300,null=False,blank=False)
    event_time = models.TextField(max_length=300,null=False,blank=False)
    event_image = models.ImageField(null=False,blank=True,upload_to="images/")
    like = models.BooleanField(default=False)
