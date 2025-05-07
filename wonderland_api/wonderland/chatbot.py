import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

RASA_URL = 'https://portfolio-myrabbithole.up.railway.app/webhooks/rest/webhook'

@csrf_exempt
def chatbot_response(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        message = data.get('message')
        sender = data.get('sender', 'user')
        response = requests.post(
            RASA_URL,
            json={"sender": sender, "message": message}
        )
        bot_responses = response.json()
        if bot_responses:
            reply = bot_responses[0].get("text", "")
        else:
            reply = "I didn't quite get that. Can you rephrase?"

        return JsonResponse({"response": reply})