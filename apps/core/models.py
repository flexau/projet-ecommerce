
from django.db import models


class ContactRequest(models.Model):

    STATUS_CHOICES = [
        ("NEW", "Nouvelle"),
        ("PROCESSING", "En cours de traitement"),
        ("COMPLETED", "Traitée"),
    ]

    name = models.CharField(
        max_length=150,
        verbose_name="Nom complet"
    )

    email = models.EmailField(
        verbose_name="Adresse e-mail"
    )

    phone = models.CharField(
        max_length=30,
        verbose_name="Téléphone"
    )

    subject = models.CharField(
        max_length=200,
        verbose_name="Sujet"
    )

    message = models.TextField(
        verbose_name="Message"
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="NEW",
        verbose_name="Statut"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Demande de contact"
        verbose_name_plural = "Demandes de contact"

    def __str__(self):
        return f"{self.name} - {self.subject}"
