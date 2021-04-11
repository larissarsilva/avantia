from .models import User
from .serializers import UserSerializer

from rest_framework import generics 
from rest_framework import filters

#Listar usuário
class ListUser(generics.ListAPIView):
    filter_backends = [filters.SearchFilter]
    search_fields = ['username','first_name','last_name']

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
