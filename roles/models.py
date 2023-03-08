from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
#from profiles.models import Profile


class Role(models.Model):
    #owner = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.BooleanField(default=True)
    teacher = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return f"extra permissions--> teacher: {self.teacher}, admin: {self.admin}"
        #return f"{self.owner} extra permissions--> teacher: {self.teacher}, admin: {self.admin}"

#def create_role(sender, instance, created, **kwargs):
 #   if created:
  #      Role.objects.create(owner=instance)


#post_save.connect(create_role, sender=User)   
