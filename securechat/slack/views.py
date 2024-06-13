import json
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from slack.models import Regex
from slack.tasks import process_data_leak

@csrf_exempt
def slack(request: HttpRequest):
    message = json.loads(request.body.decode('utf-8'))
    if 'challenge' in message:
        return JsonResponse({'challenge': message['challenge']})

    if 'event' in message and 'text' in message['event']:
        process_data_leak.delay(message['event']['text'], message['event']['channel'], message['event']['ts'], 
                            [regex.entry for regex in Regex.objects.all()])

    return HttpResponse(status=200)
