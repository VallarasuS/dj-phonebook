from django.urls import path
from . import views

urlpatterns = [
    path("contacts", views.contacts, name="contacts"),
    path("delete-contact/<int:pk>", views.delete_contact, name="delete-contact")
]