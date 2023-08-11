# Generated by Django 4.2 on 2023-08-11 03:57

import django.core.validators
import django.db.models.deletion
import localflavor.us.models
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Registration",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "number",
                    models.CharField(
                        help_text="Enter the vehicle's registration number",
                        max_length=20,
                    ),
                ),
                (
                    "state",
                    localflavor.us.models.USStateField(
                        help_text="Enter the two letter code of the registration state",
                        max_length=2,
                    ),
                ),
                (
                    "exp_date",
                    models.DateField(help_text="Registration expiration date"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Vehicle",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "year",
                    models.PositiveIntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(1880),
                            django.core.validators.MaxValueValidator(2024),
                        ]
                    ),
                ),
                (
                    "make",
                    models.CharField(
                        help_text="Enter the vehicle's make.", max_length=50
                    ),
                ),
                (
                    "model",
                    models.CharField(
                        help_text="Enter the vehicle's model.", max_length=50
                    ),
                ),
                (
                    "capacity",
                    models.PositiveIntegerField(
                        help_text="How many passengers does the vehicle hold?"
                    ),
                ),
                (
                    "mileage",
                    models.PositiveIntegerField(
                        help_text="What's the current mileage of the vehicle?"
                    ),
                ),
                (
                    "service_date",
                    models.DateField(
                        help_text="Enter when the vehicle was last serviced"
                    ),
                ),
                (
                    "registration",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="vehicles.registration",
                    ),
                ),
            ],
        ),
    ]