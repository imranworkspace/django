from django.db import models

# Create your models here.
class AuthorModel(models.Model):
    author_name=models.CharField(max_length=25)
    author_mob=models.IntegerField()

    def __str__(self):
        return self.author_name

class PostModel(models.Model):
    author=models.ForeignKey(AuthorModel,on_delete=models.CASCADE)
    post_title=models.CharField(max_length=25)
    post_description=models.TextField()
    current_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post_title