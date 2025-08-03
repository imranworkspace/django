from django.db import models
from django.contrib.auth.models import User

class PostModel(models.Model):
    # user=models.ForeignKey(User,on_delete=models.PROTECT)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post_title=models.CharField(max_length=15)
    post_description=models.TextField()
    current_datetime=models.DateTimeField(auto_now=True)
    update_datetime=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post_title