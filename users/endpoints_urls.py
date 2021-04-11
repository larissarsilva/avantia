from django.urls import path
from users.endpoints import ListUser, CreateUser, RetrieveUpdateDestroyUser

app_name = 'users'

urlpatterns = [
    path('user/',ListUser.as_view()),
    path('create-user',CreateUser.as_view()),
    path('edit-user/<int:pk>',RetrieveUpdateDestroyUser.as_view()),
  
]
