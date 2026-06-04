from django.urls import path
from . import views

urlpatterns = [
    path("", views.contacts, name="contacts"),
    path("contacts", views.contacts, name="contacts"),
    path("contact/<int:pk>/delete", views.delete_contact, name="delete-contact"),
    path("contact/<int:pk>/update", views.update_contact, name="update-contact")
]