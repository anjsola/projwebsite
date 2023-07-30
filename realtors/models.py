from django.db import models
from datetime import datetime

class Realtor(models.Model):
   name = models.CharField(max_length=200, default='DEFAULT VALUE')
   photo = models.ImageField(upload_to='photos/%Y/%m/%d/', default='DEFAULT VALUE')
   description = models.TextField(blank=True)
   email = models.CharField(max_length=20, default='DEFAULT VALUE')
   phone = models.CharField(max_length=50, default='DEFAULT VALUE')
   is_mvp = models.BooleanField(default=False)
   hire_date = models.DateTimeField(default=datetime.now, blank=True)
   def __str__(self):
     return self.name
