from django.shortcuts import render


def home(request):
    """Render the CDKBusness public homepage."""
    featured_vehicles = [
        {"brand": "Toyota", "name": "Land Cruiser", "year": 2024, "price": "72 000 $", "category": "SUV", "image": "https://images.unsplash.com/photo-1519641471654-76ce0107ad1b?auto=format&fit=crop&w=900&q=85"},
        {"brand": "BMW", "name": "Série 5", "year": 2023, "price": "65 000 $", "category": "Berline", "image": "https://images.unsplash.com/photo-1555215695-3004980ad54e?auto=format&fit=crop&w=900&q=85"},
        {"brand": "Mercedes-Benz", "name": "GLC", "year": 2024, "price": "68 000 $", "category": "SUV", "image": "https://images.unsplash.com/photo-1618843479313-40f8afb4b4d8?auto=format&fit=crop&w=900&q=85"},
        {"brand": "Audi", "name": "Q5", "year": 2023, "price": "62 000 $", "category": "SUV", "image": "https://images.unsplash.com/photo-1606664515524-ed2f786a0bd6?auto=format&fit=crop&w=900&q=85"},
    ]
    return render(request, "core/home.html", {"featured_vehicles": featured_vehicles})
