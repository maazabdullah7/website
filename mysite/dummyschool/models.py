from django.db import models


class Data(models.Model):
    name = models.CharField(max_length=100,)
    phone = models.IntegerField(default=0)
    email = models.CharField(max_length=256)
    message = models.CharField(max_length=1500)

    def __str__(self):
        return self.name