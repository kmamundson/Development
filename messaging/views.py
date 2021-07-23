from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import User, Friendship, Message, MessageRecipients

class IndexView(generic.ListView):
    template_name = 'messaging/index.html'
    context_object_name = 'user_list'
    
    def get_queryset(self):
        return User.objects.all()

def  DetailView(request, user_id):
        user = User.objects.get(pk = user_id)
        sent_messages = Message.objects.filter(sender = user)
        return render(request, 'messaging/detail.html', {
            'user': user,
            'sent_messages': sent_messages,
        })
        
def AddFriend(request, user_id):
    user = get_object_or_404(User, pk = user_id)
    
    if (user == False):
        return render(request, 'messaging/detail.html', {
            'user': user,
            'error_message': "Could not find user",
        })
    else:
        possible_friends_list = User.objects.all().exclude(pk=user_id)
        possible_friends_list
        return render(request, 'messaging/add_friend.html', {
            'user': user,
            'possible_friends_list': possible_friends_list
        })
        
def RemoveFriend(request, user_id):
    user = get_object_or_404(User, pk = user_id)
    
    if (user == False):
        return render(request, 'messaging/detail.html', {
            'user': user,
            'error_message': "Could not find user",
        })
    else:
        friends_list = user.friends.all
        return render(request, 'messaging/remove_friend.html', {
            'user': user,
            'friends_list': friends_list
        })
    
def CreateFriendship(request, request_id, user_id):
    from_user = User.objects.get(id=user_id)
    to_user = User.objects.get(id=request_id)

    friendship, created = Friendship.objects.get_or_create(from_user=from_user, to_user=to_user)
    friendship.from_user.friends.add(friendship.to_user)
    friendship.to_user.friends.add(friendship.from_user)
    friendship.delete()
    if created:
        return render(request, 'messaging/detail.html', {
            'user': from_user,
        })
    else:
        return render(request, 'messaging/add_friend.html', {
            'user': from_user,
        })
        
def DestroyFriendship(request, request_id, user_id):
    from_user = User.objects.get(id=user_id)
    to_user = User.objects.get(id=request_id)
    from_user.friends.remove(from_user)
    to_user.friends.remove(to_user)

    return render(request, 'messaging/detail.html', {
        'user': from_user,
    })

def AddMessage(request, user_id):
    user = get_object_or_404(User, pk = user_id)
    
    if (user == False):
        return render(request, 'messaging/detail.html', {
            'user': user,
            'error_message': "Could not find user",
        })
    else:
        return render(request, 'messaging/add_message.html', {
            'user': user,
        })
        
def CreateMessage(request, user_id):
    sender = User.objects.get(id=user_id)
    subject_text = request.POST["subject_text"]
    message_text = request.POST["message_text"]
    new_message, created = Message.objects.get_or_create(subject_text=subject_text, message_text=message_text, sender=sender)
    if created:
        for recipient_id in request.POST["choice"]:
            recipient = User.objects.get(id=recipient_id)
            message_recipients = MessageRecipients.objects.get_or_create(message=new_message, recipient=recipient)
        return render(request, 'messaging/detail.html', {
            'user': sender,
        })
    else:
        return render(request, 'messaging/add_message.html', {
            'user': sender,
        })
        

    
    
    