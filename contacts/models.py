from django.db import models

# Create your models here.
class Contact(models.Model):

    name = models.CharField()
    phone = models.CharField()

    def __str__(self):
        return f"{self.name} : {self.phone}"