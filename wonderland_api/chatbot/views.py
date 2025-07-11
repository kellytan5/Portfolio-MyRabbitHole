# chatbot/views.py
import os
import nltk
from django.http import JsonResponse
from .nlp import chatbot

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
nltk.data.path.append(os.path.join(BASE_DIR, '..', 'nltk_data'))

def chatbot_response(request):
    user_input = request.GET.get("message").lower()
    if not user_input:
        return JsonResponse({"response": "Please enter a message."}, status=400)

    response = chatbot.get_response(user_input)
    return JsonResponse({"response": response})