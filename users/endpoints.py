from .models import User
from .serializers import UserSerializer

from rest_framework import generics 

#Listar usuário
class ListUser(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

#Criar usuário
class CreateUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

#Editar e Excluir usuário
class RetrieveUpdateDestroyUser(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer       
