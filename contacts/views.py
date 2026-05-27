from django.shortcuts import render

from .models import Contact

# Create your views here.

def contacts(request):

    contacts = Contact.objects.all()
    context = { "contacts": contacts }

    return render(request, "contacts.html", context)