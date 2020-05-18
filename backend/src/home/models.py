from django.db import models
import datetime
# Create your models here

class User(models.Model):
    name = models.CharField(max_length=40)
    date = models.DateTimeField(datetime.date.today())

    def __str__(self):
        return self.name