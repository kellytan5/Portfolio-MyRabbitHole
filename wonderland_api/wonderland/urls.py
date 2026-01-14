from django.urls import path 
from .views.edu_view import edu_view
from .views.exp_view import exp_view
from .views.projects_view import projects_view

# define the urls
urlpatterns = [
    path('education/', edu_view, name='education'),
    path('experiences/', exp_view, name='experiences'),
    path('projects/', projects_view, name='projects')
]