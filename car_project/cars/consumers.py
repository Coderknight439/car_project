import json
from channels.generic.websocket import AsyncJsonWebsocketConsumer


class CarDataConsumer(AsyncJsonWebsocketConsumer):
	
	async def connect(self):
		await self.accept()
	
	async def disconnect(self, close_code):
		print("Disconnected")
	
	async def receive(self, text_data=None, bytes_data=None, **kwargs):
		"""
		Receive message from WebSocket.
		Get the event and send the appropriate event
		"""
		response = json.loads(text_data)
		event = response.get("event", None)
	
		if event == 'START':
			print("Connection Started")
		
	async def send_message(self, res):
		""" Receive message from event"""
		# Send message to WebSocket
		await self.send(text_data=json.dumps({
			"payload": res,
		}))
