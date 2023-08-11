import datetime

from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from localflavor.us.models import USStateField


class Registration(models.Model):
    """Model representing a vehicle's registration"""

    number = models.CharField(
        max_length=20, help_text="Enter the vehicle's registration number"
    )
    state = USStateField(
        help_text="Enter the two letter code of the registration state"
    )
    exp_date = models.DateField(help_text="Registration expiration date")

    def __str__(self):
        return self.number


class Vehicle(models.Model):
    """Model representing a specific vehicle in the fleet"""

    registration = models.OneToOneField(
        "Registration", on_delete=models.CASCADE, null=True, blank=True
    )
    year = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1880),
            MaxValueValidator(datetime.date.today().year + 1),
        ]
    )
    make = models.CharField(max_length=50, help_text="Enter the vehicle's make.")
    model = models.CharField(max_length=50, help_text="Enter the vehicle's model.")
    vehicle_type = [
        ("SED", "Sedan"),
        ("VAN", "Van"),
        ("SUV", "SUV"),
    ]
    capacity = models.PositiveIntegerField(
        help_text="How many passengers does the vehicle hold?"
    )
    mileage = models.PositiveIntegerField(
        help_text="What's the current mileage of the vehicle?"
    )
    fuel_type = [
        ("D", "Diesel"),
        ("G", "Gas"),
        ("E", "Electric"),
    ]
    service_date = models.DateField(
        help_text="Enter when the vehicle was last serviced"
    )

    def clean_service_date(self):
        data = self.cleaned_data["service_date"]

        # Check if a date is not in the future.
        if data > datetime.date.today():
            raise ValidationError(("Invalid date - service date in the future"))

        return data

    def __str__(self):
        """String for representing the Model object."""
        if self.registration:
            return f"{self.year} {self.make} {self.model} -- {self.registration.number}"
        else:
            return f'{self.year} {self.make} {self.model} -- {"UNREGISTERED"}'
