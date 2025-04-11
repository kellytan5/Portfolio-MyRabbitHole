from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.parsers import MultiPartParser, FormParser

# API definition for serializers 
from .serializers import *
# import models 
from .models import *

# Create your views here.

# CRUD Contacts 
class ContactAPIView(viewsets.ModelViewSet):
  # get all contacts
  queryset = Contact.objects.all()
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
  
  def post(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    
    if serializer.is_valid():
      # Save the contact message to the database
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
      # If validation fails, return errors
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
# CRUD Project
class ProjectViewSet(viewsets.ModelViewSet):
  images = ProjectImageSerializer(many=True)  # Nest images inside project data
  queryset = Project.objects.all()
  serializer_class = ProjectSerializer
  permission_classes = [AllowAny]

  def list(self, request):
    data = self.get_queryset()
    serializer = self.get_serializer(data, many=True)
    return Response(serializer.data)

  def retrieve(self, request, pk=None):
    instance = self.get_object()
    serializer = self.get_serializer(instance)
    return Response(serializer.data)

class ProjectImageViewSet(viewsets.ModelViewSet):
  queryset = ProjectImage.objects.all()
  serializer_class = ProjectImageSerializer
  parser_classes = (MultiPartParser, FormParser)  # Allows image uploads
  def create(self, request, *args, **kwargs):
    """Handle multiple image uploads"""
    images = request.FILES.getlist('image')  # Get multiple files
    project_id = request.data.get("project")  # Get project ID
    if not project_id:
        return Response({"error": "Project ID is required"}, status=status.HTTP_400_BAD_REQUEST)
    try:
        p = Project.objects.get(id=project_id)
    except Project.DoesNotExist:
        return Response({"error": "Project not found"}, status=status.HTTP_404_NOT_FOUND)
    for image in images:
        ProjectImage.objects.create(project=p, image=image)
    return Response({"message": "Images uploaded successfully"}, status=status.HTTP_201_CREATED)
  
  def get(self, request, project_id): 
    # You can use `project_id` directly because it's passed from the URL
    try:
      project = Project.objects.get(id=project_id)
      project_images = project.images.all()  # Get all images for this project
      image_serializer = ProjectImageSerializer(project_images, many=True)
      return JsonResponse({'project': project.name, 'images': image_serializer.data})
    except Project.DoesNotExist:
      return JsonResponse({'error': 'Project not found'}, status=404)
  
# CRUD Education 
class EducationAPIView(viewsets.ModelViewSet):
  # get all educations
  queryset = Education.objects.all()
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
  queryset = Experience.objects.all()
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
