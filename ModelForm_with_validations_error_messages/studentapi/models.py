from django.db import models

# Create your models here.
class StudentModel(models.Model):
    name=models.CharField(max_length=25)
    email=models.EmailField()
    password=models.CharField(max_length=16)

    def __str__(self) -> str:
        return self.name