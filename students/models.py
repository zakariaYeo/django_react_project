from django.db import models


# Create your models here.

class Student(models.Model):
    name = models.CharField("Name", max_length=200)
    email = models.EmailField("Email")
    document = models.CharField("Document", max_length=50)
    phone = models.CharField("Phone", max_length=11)
    registrationDate = models.DateField("Registration date", auto_now_add=True)

    def __str__(self):
        return self.name
