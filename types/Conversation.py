# import time
# from monogram.bot.methods.sendMessage import send_message
# from monogram.bot.types import Message
#
# class Conversation:
#     def __init__(self, message: Message, timeout=60):
#         self.chat_id = message.chat.id
#         self.timeout = timeout
#         self.start_time = None
#         self.is_active = None
#
#     def __enter__(self):
#         print('enter')
#         self.is_active = True
#         self.start_time = time.time()
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('Exited conversation')
#         self.is_active = False
#
#     def answer(self, text: str, keyboard=None):
#         if keyboard:
#             send_message(chat_id=self.chat_id, text=text, reply_markup=keyboard)
#         else:
#             send_message(chat_id=self.chat_id, text=text)
#
#     def start(self):
#         elapsed_time = time.time() - self.start_time
#         if elapsed_time > self.timeout:
#             self.is_active = False
#             print("Conversation closed due to inactivity.")
#         else:
#             time.sleep(self.timeout - elapsed_time)
#
#     def cancel(self):
#         self.is_active = False
#         print("Conversation cancelled.")
