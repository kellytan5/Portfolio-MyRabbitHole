from django.http import JsonResponse
from ..data.projects import PROJECTS

def projects_view(request): 
  return JsonResponse(PROJECTS, safe=False)

