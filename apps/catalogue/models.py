
from django.db import models


class Vehicle(models.Model):
    TRANSMISSION_CHOICES = [
        ("MANUAL", "Manuelle"),
        ("AUTOMATIC", "Automatique"),
    ]

    FUEL_CHOICES = [
        ("PETROL", "Essence"),
        ("DIESEL", "Diesel"),
        ("ELECTRIC", "Électrique"),
        ("HYBRID", "Hybride"),
    ]

    name = models.CharField(max_length=150, verbose_name="Nom du véhicule")
    brand = models.CharField(max_length=100, verbose_name="Marque")
    model = models.CharField(max_length=100, verbose_name="Modèle")
    year = models.PositiveIntegerField(verbose_name="Année")
    price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Prix")
    mileage = models.PositiveIntegerField(default=0, verbose_name="Kilométrage")
    transmission = models.CharField(
        max_length=20,
        choices=TRANSMISSION_CHOICES,
        verbose_name="Transmission",
    )
    fuel = models.CharField(
        max_length=20,
        choices=FUEL_CHOICES,
        verbose_name="Carburant",
    )
    description = models.TextField(blank=True, verbose_name="Description")
    image = models.ImageField(
        upload_to="vehicles/",
        blank=True,
        null=True,
        verbose_name="Photo",
    )
    available = models.BooleanField(default=True, verbose_name="Disponible")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Véhicule"
        verbose_name_plural = "Véhicules"

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"

