
from django.shortcuts import render, redirect
from django.contrib import messages
from apps.catalogue.models import Vehicle
from .models import ContactRequest


def home(request):
    featured_vehicles = Vehicle.objects.filter(
        available=True
    ).order_by("-created_at")[:4]

    return render(
        request,
        "core/home.html",
        {"featured_vehicles": featured_vehicles}
    )


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        phone = request.POST.get("phone", "").strip()
        subject = request.POST.get("subject", "").strip()
        message = request.POST.get("message", "").strip()

        if not all([name, email, phone, subject, message]):
            messages.error(
                request,
                "Veuillez remplir tous les champs."
            )
            return redirect("core:contact")

        ContactRequest.objects.create(
            name=name,
            email=email,
            phone=phone,
            subject=subject,
            message=message
        )

        messages.success(
            request,
            "Votre demande a été envoyée avec succès. Merci !"
        )

        return redirect("core:contact")

    return render(request, "core/contact.html")
