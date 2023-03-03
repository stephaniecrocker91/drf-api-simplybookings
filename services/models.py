from django.db import models

# Create your models here.

class Service(models.Model):
    service = models.CharField(max_length=255)
    image = models.ImageField(
        upload_to="images/", default="../imresizer-1677838586928_dfojm5"
    )
    content = models.TextField(blank=True)

    class Meta:
        ordering = ['service']

    def __str__(self):
        return f"Service: {self.service}"