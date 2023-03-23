import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class ShopConsumer(WebsocketConsumer):

    def connect(self):
        self.room_name = 'test_room_name'
        self.room_group_name = 'test_group_name'

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name)

    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        """Принимает данные"""
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {'type': 'chat_message',
             'message': message}
            )

    def chat_message(self, event):
        """Отправляет Данные Клиенту"""
        message = event['message']

        self.send(text_data=json.dumps({
            'event': 'Send',
            'message:': message
        }))


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data = '{"message": "dssssss"}'
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        self.send(text_data=json.dumps({"message": message}))