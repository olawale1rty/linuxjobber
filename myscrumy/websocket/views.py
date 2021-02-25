from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import ChatMessage, Connection 
# Create your views here.

@csrf_exempt
def test(request):
	return JsonResponse({'message': 'hello Daud'}, status=200)

def _parse_body(body):
	body_unicode = body.decode('utf-8')
	return json.loads(body_unicode)

@csrf_exempt
def connect(request):
	body = _parse_body(request.body)
	connection_id = body['connectionId']
	connection_saved = Connection(connection_id=connection_id)
	connection_saved.save()
	return JsonResponse({'message': 'connect successfully'}, status=200)

@csrf_exempt
def disconnect(request):
	body = _parse_body(request.body)
	connection_id = body['connectionId']
	connection_saved = Connection.objects.get(connection_id=connection_id)
	connection_saved.delete()
	return JsonResponse({'message': 'disconnect successfully'}, status=200)