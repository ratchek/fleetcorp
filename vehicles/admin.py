from django.contrib import admin

from .models import Registration, Vehicle

# Register your models here.
admin.site.register(Vehicle)
admin.site.register(Registration)
