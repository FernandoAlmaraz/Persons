from django.db import models


# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)

    def __str__(self):
        return f"Persona ({self.id}): {self.name} {self.last_name} - {self.email}"
