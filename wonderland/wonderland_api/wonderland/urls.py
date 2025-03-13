from django.urls import path 
from .views import *

# define the urls
urlpatterns = [
    path('contacts/', ContactAPIView.as_view({'get': 'list'}), name="contact_list"),
    path('contacts/<int:pk>/', ContactAPIView.as_view({'get': 'retrieve'}), name="contact_retrieve"),
    path('edu_list/', EducationAPIView.as_view({'get': 'list'}), name="edu_list"),
    path('edu_list/<int:pk>/', EducationAPIView.as_view({'get': 'retrieve'}), name="edu_retrieve"),
    path('exp_list/', ExpAPIView.as_view({'get': 'list'}), name="exp_list"),
    path('exp_list/<int:pk>/', ExpAPIView.as_view({'get': 'retrieve'}), name="exp_retrieve"),
]