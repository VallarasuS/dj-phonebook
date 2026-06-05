from django.shortcuts import render, redirect

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

def delete_contact(request, pk):
    contact = Contact.objects.get(pk=pk)
    contact.delete()

    return redirect("contacts")

def update_contact(request, pk):
    
    if request.method == "POST":

        phone = request.POST.get("phone")
        name = request.POST.get("name")

        contact = Contact.objects.get(pk=pk)
        contact.phone = phone
        contact.name = name
        contact.save()

        return redirect("contacts")

    contact = Contact.objects.get(pk=pk)
    return render(request, "edit.html", { "contact" : contact })