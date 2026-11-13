
from django.shortcuts import render, get_object_or_404
from .models import Vehicle


def catalogue(request):
    vehicles = Vehicle.objects.filter(available=True)

    search = request.GET.get("q", "")
    brand = request.GET.get("brand", "")
    fuel = request.GET.get("fuel", "")

    if search:
        vehicles = vehicles.filter(
            name__icontains=search
        ) | vehicles.filter(
            brand__icontains=search
        ) | vehicles.filter(
            model__icontains=search
        )

    if brand:
        vehicles = vehicles.filter(brand__iexact=brand)

    if fuel:
        vehicles = vehicles.filter(fuel=fuel)

    brands = Vehicle.objects.filter(
        available=True
    ).values_list("brand", flat=True).distinct()

    return render(request, "catalogue/catalogue.html", {
        "vehicles": vehicles,
        "brands": brands,
        "search": search,
        "selected_brand": brand,
        "selected_fuel": fuel,
    })


def vehicle_detail(request, pk):
    vehicle = get_object_or_404(
        Vehicle,
        pk=pk,
        available=True
    )

    return render(request, "catalogue/detail.html", {
        "vehicle": vehicle
    })
