from django.contrib import admin

from .models import Person, Car


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'age')


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'year')
