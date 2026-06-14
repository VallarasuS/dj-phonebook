from django.shortcuts import render
import rest_framework
from rest_framework.views import APIView
from rest_framework.response import Response

from contacts.models import Contact
from .serializers import ContactSerializer

# Create your views here.
class ContactAPIView(APIView):
    
    def get(self, request, pk, format=None):
        
        contact = Contact.objects.get(pk=pk)
        serializer = ContactSerializer(contact)

        return Response(serializer.data)

    def delete(self, request, pk):
        contact = Contact.objects.get(pk=pk)
        contact.delete()

        return Response(contact.id, status=200)

    def put(self, request, pk):
        contact = Contact.objects.get(pk=pk)
        serializer = ContactSerializer(contact, data=request.data)
        serializer.save()

        return Response(serializer.data)