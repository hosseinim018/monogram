import pickle
from django.db import models

class Conversation(models.Model):
    user_id = models.PositiveIntegerField()  # User ID as a positive integer
    callback_data = models.CharField(max_length=255, blank=True, null=True)
    status = models.BooleanField(default=True)  # Conversation open status

    def __str__(self):
        return f"Conversation with user ID {self.user_id} (closed: {self.status}) (callback_data: {self.callback_data})"  # String representation
