from django.shortcuts import render

# Create your views here.
from vehicles.models import Registration, Vehicle


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_vehicles = Vehicle.objects.all().count()
    num_registrations = Registration.objects.all().count()

    # Available books (status = 'NY')
    num_ny_vehicles = Registration.objects.filter(state__exact="NY").count()

    context = {
        "num_vehicles": num_vehicles,
        "num_registrations": num_registrations,
        "num_ny_vehicles": num_ny_vehicles,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, "index.html", context=context)
