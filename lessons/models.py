from django.db import models
from django.utils import timezone
from services.models import Service

class Lesson(models.Model):
    lesson = models.CharField(unique=True, max_length=255)
    description = models.TextField(blank=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to="images/", default="../imresizer-1677838586928_dfojm5"
    )
    teacher = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    starts_at = models.TimeField()
    ends_at = models.TimeField()
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['starts_at']

    def __str__(self):
        return f"{self.lesson}: from {self.starts_at} to {self.ends_at}"
