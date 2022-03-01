from django.db import models

# Create your models here.
class Icecream(models.Model):
    flavor = models.CharField(max_length=100)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.flavor

    