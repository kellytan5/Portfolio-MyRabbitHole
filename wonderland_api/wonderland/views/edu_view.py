from django.http import JsonResponse
from ..data.education import EDUCATION

def edu_view(request): 
  return JsonResponse(EDUCATION, safe=False)