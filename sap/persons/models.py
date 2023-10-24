from django.db import models


# Create your models here.


class Home(models.Model):
    street = models.CharField(max_length=250)
    no_street = models.IntegerField()
    country = models.CharField(max_length=250)

    def __str__(self):
        return (
            f"Domicilio({self.id}): {self.street} - {self.no_street} - {self.country}"
        )


class Person(models.Model):
    name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    home = models.ForeignKey(Home, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Persona ({self.id}): {self.name} {self.last_name} - {self.email}"
