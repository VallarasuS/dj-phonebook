from django.urls import path
from .views import ContactAPIView

urlpatterns = [
    path("contact/<int:pk>", ContactAPIView.as_view(), name="contact-api-view" )
]