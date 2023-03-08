from django.db import models
from django.contrib.auth.models import User
##from profiles.models import Profile


class Role(models.Model):
    user = models.BooleanField(default=True)
    teacher = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return f"teacher: {self.teacher}, admin: {self.admin}"
