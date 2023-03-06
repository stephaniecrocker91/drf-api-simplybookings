from django.db import models

class Lesson(models.Model):
    lesson = models.CharField(unique=True)
    service = models.ForeignKey(service, on_delete=models.CASCADE)
    
