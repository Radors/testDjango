from django.db import models

# Create your models here.


class WelcomeMessage(models.Model):
    message = models.CharField(max_length=200)


