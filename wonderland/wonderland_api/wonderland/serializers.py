from rest_framework import routers,serializers,viewsets 
from .models import contact, education, experience

class ContactSerializer(serializers.HyperlinkedModelSerializer):
  class Meta: 
    model = contact 
    fields = ['id', 'name', 'email', 'message', 'created_at']

class EduSerializer(serializers.HyperlinkedModelSerializer):
  class Meta: 
    model = education
    fields = ['id', 'title', 'description', 'location', 'duration', 'image', 'name', 'position', 'link']

class ExpSerializer(serializers.HyperlinkedModelSerializer):
  class Meta: 
    model = experience
    fields = ['id', 'date', 'title', 'company', 'description', 'location']