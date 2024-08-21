from django.db import models

class AI_Detection(models.Model):
    text = models.TextField()
    prediction = models.FloatField(null=True, blank=True)