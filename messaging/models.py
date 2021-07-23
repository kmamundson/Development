import datetime

from django.db import models
from django.utils import timezone

class User(models.Model):
    name = models.CharField(max_length=30)
    friends = models.ManyToManyField("User", blank=True)
    recieved_messages = models.ManyToManyField("Message", blank=True)    
    
    def __str__(self):
        return self.name

class Friendship(models.Model):
    from_user = models.ForeignKey(User, related_name='from_user', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='to_user', on_delete=models.CASCADE)
    
class Message(models.Model):
    subject_text = models.CharField(max_length=30)
    message_text = models.CharField(max_length=200)
    sender = models.ForeignKey(User, related_name='sender', on_delete=models.CASCADE)
    
    
class MessageRecipients(models.Model):
    message = models.ForeignKey(Message, related_name='message', on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, related_name='recipient', on_delete=models.CASCADE)
