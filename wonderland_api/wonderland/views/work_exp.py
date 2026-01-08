from django.http import JsonResponse
from ..data.work_exp import WORK_EXPERIENCES

def projects_view(request): 
  return JsonResponse(WORK_EXPERIENCES, safe=False)