from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

# API definition for serializers 
from .serializers import *
# import models 
from .models import *

# Create your views here.

# CRUD Contacts 
class ContactAPIView(viewsets.ModelViewSet):
  # get all contacts
  queryset = contact.objects.all()
  # serialize the education data 
  serializer_class = ContactSerializer
  permission_classes = [AllowAny]

  def list(self, request):
    data = self.get_queryset()
    serializer = self.get_serializer(data, many=True)
    return Response(serializer.data)

  def retrieve(self, request, pk=None):
    instance = self.get_object()
    serializer = self.get_serializer(instance)
    return Response(serializer.data)
  
# CRUD Education 
class EducationAPIView(viewsets.ModelViewSet):
  # get all educations
  queryset = education.objects.all()
  # serialize the education data 
  serializer_class = EduSerializer
  permission_classes = [AllowAny]

  def list(self, request):
    data = self.get_queryset()
    serializer = self.get_serializer(data, many=True)
    return Response(serializer.data)

  def retrieve(self, request, pk=None):
    instance = self.get_object()
    serializer = self.get_serializer(instance)
    return Response(serializer.data)
  
# CRUD Experience 
class ExpAPIView(viewsets.ModelViewSet):
  # get all experience
  queryset = experience.objects.all()
  # serialize the education data 
  serializer_class = ExpSerializer
  permission_classes = [AllowAny]

  def list(self, request):
    data = self.get_queryset()
    serializer = self.get_serializer(data, many=True)
    return Response(serializer.data)

  def retrieve(self, request, pk=None):
    instance = self.get_object()
    serializer = self.get_serializer(instance)
    return Response(serializer.data)