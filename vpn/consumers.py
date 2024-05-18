# consumers.py
import asyncio
import json
import psutil

from channels.generic.websocket import AsyncWebsocketConsumer


# def get_cpu_load():
#     # your code here
#     return psutil.cpu_percent()


# def get_ram_usage():
#     # your code here
#     return psutil.virtual_memory().percent


# class StatusConsumer(AsyncWebsocketConsumer):

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.is_disconnecting = False

#     async def connect(self):
#         await self.accept()

#         while not self.is_disconnecting:
#             cpu_load = get_cpu_load()  # replace with your function
#             ram_usage = get_ram_usage()  # replace with your function

#             await self.send(json.dumps({
#                 'cpu_load': cpu_load,
#                 'ram_usage': ram_usage,

#             }))
#             await asyncio.sleep(10)

#         await self.close()

#     async def disconnect(self, close_code):
#         self.is_disconnecting = True
