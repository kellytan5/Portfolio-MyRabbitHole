from django.urls import path 
from .views import *

# define the urls
urlpatterns = [
    path('contacts_list/', ContactAPIView.as_view({'get': 'list'}), name="contact_list"),
    path('contacts/<int:pk>/', ContactAPIView.as_view({'get': 'retrieve'}), name="contact_retrieve"),
    path('new_contact/', ContactAPIView.as_view({'post': 'post'}), name="new_contact"),
    path('edu_list/', EducationAPIView.as_view({'get': 'list'}), name="edu_list"),
    path('edu/<int:pk>/', EducationAPIView.as_view({'get': 'retrieve'}), name="edu_retrieve"),
    path('exp_list/', ExpAPIView.as_view({'get': 'list'}), name="exp_list"),
    path('exp/<int:pk>/', ExpAPIView.as_view({'get': 'retrieve'}), name="exp_retrieve"),
    path('project_list/', ProjectViewSet.as_view({'get': 'list'}), name="project_list"),
    path('projects/<int:pk>/', ProjectViewSet.as_view({'get': 'retrieve'}), name="project_retrieve"),
    path('api/project-images/<int:project_id>/', ProjectImageViewSet.as_view({'get': 'get'}), name='project-images'),
]