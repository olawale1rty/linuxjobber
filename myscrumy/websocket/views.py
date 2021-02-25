from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import ChatMessage, Connection
from django.core.serializers import serialize
import boto3 
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

def _send_to_connection(connection_id, data):
	gatewayapi = boto3.client('apigatewaymanagementapi', endpoint_url='https://vlb431qo61.execute-api.us-east-2.amazonaws.com/test/',
		region_name='us-east-2',aws_access_key_id='AKIATC5Y3PONHHAOLFVT', aws_secret_access_key='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')
	return gatewayapi.post_to_connection(ConnectionId=connection_id, Data=json.dumps(data).encode('utf-8'))

def _send_to_connection_2(connection_id, data):
	gatewayapi = boto3.client('apigatewaymanagementapi', endpoint_url='https://vlb431qo61.execute-api.us-east-2.amazonaws.com/test/',
		region_name='us-east-2',aws_access_key_id='AKIATC5Y3PONHHAOLFVT', aws_secret_access_key='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')
	return gatewayapi.post_to_connection(ConnectionId=connection_id, Data=data)
 
@csrf_exempt
def send_message(request):
	body_main = _parse_body(request.body)
	body = body_main['body']
	username = body['username']
	message = body['message']
	timestamp = body['timestamp']
	message_input = ChatMessage(username=username, message=message, timestamp=timestamp)
	message_input.save()
	connections = Connection.objects.all()
	data = {'messages':[body]}
	for i in connections:
		_send_to_connection(i.connection_id, data)	

@csrf_exempt
def recent_messages(request):
	body = _parse_body(request.body)
	connection_id = body['connectionId']
	messages = ChatMessage.objects.all().order_by('-pk')
	output = serialize("json", messages, fields=('username','message','timestamp'))
	out = []
	for i in output:
		out.append(i[2])
	data = {'messages': out}
	_send_to_connection_2(connection_id, data)