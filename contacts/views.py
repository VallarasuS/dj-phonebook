from django.shortcuts import render

from .models import Contact

# Create your views here.

def contacts(request):

    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        Contact.objects.create(name=name, phone=phone)

    contacts = Contact.objects.all()
    context = { "contacts": contacts }

    return render(request, "contacts.html", context)