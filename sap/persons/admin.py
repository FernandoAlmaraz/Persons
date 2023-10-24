from django.contrib import admin

from persons.models import Home, Person

# Register your models here.
admin.site.register(Person)
admin.site.register(Home)
