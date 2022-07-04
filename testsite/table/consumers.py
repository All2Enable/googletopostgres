import json
from channels.generic.websocket import WebsocketConsumer

from channels.layers import get_channel_layer
from .db_connection import updatetable
from asgiref.sync import async_to_sync


class TableConsumer(WebsocketConsumer):
    channel_layer = get_channel_layer()
    room_group_name = 'front'
    channel_name = 'websocket'

    def connect(self):
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name,
        )

        self.accept()
        updatetable()

        self.send(text_data=json.dumps({
            'type': 'connection_established',
            'message': 'You are now connected my brother!'
        }))

    def receive(self, text_data):
        text_data_json = text_data
        message = text_data_json
        updatetable()

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'table',
                'message': message
            }
        )

    def table(self, event):
        message = event['message']

        self.send(text_data=json.dumps({
            'type': 'table',
            'message': message
        }))
