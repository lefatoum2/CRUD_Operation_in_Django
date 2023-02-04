from django.db import models

# Create your models here.
choices2 = (('I','Infra'),('IO','In/out'),('W','Web'),('R','RPG'),('S','Support'),('R','RH'),('E','Exploitation'))
class Employee(models.Model):
    firstname = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    category = models.CharField(choices=choices2,max_length=20)
    email = models.EmailField(max_length=150)
    gender = models.CharField(choices=(('M','Male'),('F','Female')),max_length=20)
    date_of_birth = models.DateField()
    send_update = models.BooleanField(default=False)
    photo = models.FileField(upload_to='profile')

    def __str__(self) -> str:
        return self.name