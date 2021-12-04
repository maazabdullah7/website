from django.db import models


class Msg(models.Model):
    name = models.CharField(max_length=100,)
    email = models.CharField(max_length=256)
    message = models.CharField(max_length=1500)

    def __str__(self):
        return self.name

