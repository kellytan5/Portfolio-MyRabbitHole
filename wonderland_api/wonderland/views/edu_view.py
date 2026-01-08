from django.http import JsonResponse
from ..data.education import EDUCATION

def projects_view(request): 
  return JsonResponse(EDUCATION, safe=False)