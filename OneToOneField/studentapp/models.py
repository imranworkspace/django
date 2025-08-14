from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class ProfileModel(models.Model):
    # user=models.OneToOneField(User,on_delete=models.CASCADE)
    user=models.OneToOneField(User,on_delete=models.PROTECT)
    profile_name=models.CharField(max_length=25)
    city=models.CharField(max_length=25)

    def __str__(self):
        return self.profile_name

