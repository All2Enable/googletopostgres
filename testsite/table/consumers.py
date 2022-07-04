import json
from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer


# from channels.layers import get_channel_layer
# from channels.db import database_sync_to_async
# from .db_connection import updatetable
# from asgiref.sync import async_to_sync



class TableConsumer(AsyncWebsocketConsumer):

    async def websocket_connect(self, event):
    # When the connection is first opened, also send the historical data
        await self.accept()
        await self.send(text_data=json.dumps({
                'type': 'connection_established',
                'message': 'You are now connected my brother!'
            }))
        if event == 'tableupdate':
            await self.send(text_data=json.dumps({
                    'type': 'table',
                    'message': 'Well, here we are!'
                }))


    # This is what I use to send the messages with the live data
    async def stream(self, event):
        if event == 'tableupdate':
            await self.send(text_data=json.dumps({
                    'type': 'table',
                    'message': 'Well, here we are!'
                }))



# class TableConsumer(WebsocketConsumer):
#     channel_layer = get_channel_layer()
#     room_group_name = 'front'
#     channel_name = 'websocket'




    # def connect(self):
    #     async_to_sync(self.channel_layer.group_add)(
    #         self.room_group_name,
    #         self.channel_name,
    #     )
    #
    #     self.accept()
    #     while connec
    #
    #     updatetable()
    #
    #     self.send(text_data=json.dumps({
    #         'type': 'connection_established',
    #         'message': 'You are now connected my brother!'
    #     }))




        # async_to_sync(self.channel_layer.send)(
        #     self.channel_name, {
        #         'type': 'table',
        #         'message': 'Well, well, well'
        #     }
        # )

    # def sendsmth(self):
    #     updatetable()
    #
    #     self.send(text_data=json.dumps({
    #         'type': 'table',
    #         'message': 'You are now connected my brother!'
    #     }))
        # async_to_sync(self.channel_layer.send)(
        #     self.room_group_name, {
        #         'type': 'table',
        #         'message': 'Well, well, well'
        #     }
        # )
