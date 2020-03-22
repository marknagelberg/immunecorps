from django.db import models

class Volunteer(models.Model):
    email = models.EmailField(default='')

