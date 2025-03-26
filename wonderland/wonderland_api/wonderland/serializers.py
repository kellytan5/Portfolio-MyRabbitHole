from rest_framework import routers,serializers,viewsets 
from .models import *

class ContactSerializer(serializers.HyperlinkedModelSerializer):
  class Meta: 
    model = Contact 
    fields = ['id', 'name', 'email', 'message', 'created_at']

class EduSerializer(serializers.HyperlinkedModelSerializer):
  class Meta: 
    model = Education
    fields = ['id', 'title', 'description', 'location', 'start_date', 'end_date', 'image', 'name', 'position', 'link']

class ExpSerializer(serializers.HyperlinkedModelSerializer):
  class Meta: 
    model = Experience
    fields = ['id', 'start_date', 'end_date', 'title', 'company', 'description', 'location']


class ProjectImageSerializer(serializers.ModelSerializer):
  class Meta:
    model = ProjectImage
    fields = ['id', 'image', 'uploaded_at']

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
  images = ProjectImageSerializer(many=True, read_only=True)  # Nested serializer

  class Meta: 
    model = Project
    fields = ['id', 'title', 'description', 'conclusion', 'location', 'start_date', 'end_date', 'position', 'images', 'github', 'figma']