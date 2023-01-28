from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)
    gender = models.CharField(choices=(('M','Male'),('F','Female')),max_length=20)
    date_of_birth = models.DateField()
    send_update = models.BooleanField(default=False)
    photo = models.FileField(upload_to='profile')

    def __str__(self) -> str:
        return self.name