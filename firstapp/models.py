from django.db import models

class Mobile(models.Model):

    brand = models.CharField(max_length=100)

    model_name = models.CharField(max_length=100)

    price = models.IntegerField()

    ram = models.CharField(max_length=20)

    storage = models.CharField(max_length=20)

    def __str__(self):
        return self.model_name