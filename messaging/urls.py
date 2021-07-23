from django.urls import path

from . import views

app_name = 'messaging'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:user_id>/', views.DetailView, name='detail'),
    path('<int:user_id>/add_friend', views.AddFriend, name='add_friend'),
    path('<int:user_id>/remove_friend', views.RemoveFriend, name='remove_friend'),
    path('create_friendship/<int:request_id>,<int:user_id>/', views.CreateFriendship, name='create_friendship'),
    path('destroy_friendship/<int:request_id>,<int:user_id>/', views.DestroyFriendship, name='destroy_friendship'),
    path('<int:user_id>/create_message', views.CreateMessage, name='create_message'),
    path('<int:user_id>/add_message', views.AddMessage, name='add_message'),
]