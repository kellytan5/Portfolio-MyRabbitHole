# chatbot/views.py
from django.http import JsonResponse
from .nlp import chatbot

def chatbot_response(request):
    user_input = request.GET.get("message").lower()
    if not user_input:
        return JsonResponse({"response": "Please enter a message."}, status=400)

    response = chatbot.get_response(user_input)
    return JsonResponse({"response": response})