from monogram.models import Conversation as Conv
import pickle
import time



class Conversation:
    """
    Represents a conversation within a specific chat.

    A conversation keeps track of new messages since it was
    created until its exit and easily lets you query the
    current state.

    If you need a conversation across two or more chats,
    you should use two conversations and synchronize them
    as you better see fit.
    """

    def __init__(self, user_id: int,  timeout=60):
        """
        Initializes a new Conversation object.

        Args:
            message (Message): The initial message that triggered the conversation.
            timeout (int, optional): The timeout duration in seconds. Default is 60 seconds.
        """
        self.timeout = timeout
        self.start_time = None
        self.user_id = user_id

    def create(self, callback_data: str, ):
        # Create a new conversation record
        # print('Create a new conversation record')
        conversation = Conv.objects.create(user_id=self.user_id, callback_data=callback_data)

    def data(self):
        conversation = Conv.objects.filter(user_id=self.user_id)
        if conversation.exists():
            conversation = conversation.last()
            data = {
                'status': conversation.status,
                'callback_data': conversation.callback_data,
            }
            return data
    def change_callback_data(self, callback_data):
        conversation = Conv.objects.filter(user_id=self.user_id)
        if conversation.exists():
            conversation = conversation.last()
            conversation.callback_data = callback_data
            conversation.save()
    def cancel(self):
        """
        Cancels the conversation.
        """
        conversation = Conv.objects.filter(user_id=self.user_id)
        conversation.delete()
        # print("Conversation cancelled.")
        # print("Exited conversation")
        # conversation = Conversation.objects.filter(user_id=self.chat_id)
        # last_conversation = conversation.last()
        # last_conversation.status = False
        # last_conversation.save()
        # Conv.objects.filter(user_id=self.chat_id).delete()


    def get_msg(self):
        return self.conversation


# Example usage
# message = Message(chat={"id": 0, "type": "ss"}, message_id=1111, date=1111, text="slm")
# print(message)
#
# async def main():
#     async with Conversation(message) as conv:
#         print("Created conversation!")
#         # Perform conversation tasks
#         for i in range(0, 10):
#             print(i)


# asyncio.run(main())
# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())
