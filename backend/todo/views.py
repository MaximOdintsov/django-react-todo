from django.shortcuts import render

# import view sets from the REST framework
from rest_framework import viewsets

# import the TodoSerializer from the serializer file
from .serializers import TodoSerializer

# import the to_do model from the models file
from .models import Todo


# create a class for the to_do model viewsets
class TodoView(viewsets.ModelViewSet):

    # create a serializer class and assign it to the TodoSerializer class
    serializer_class = TodoSerializer

    # define a variable and populate it with the to_do list objects
    queryset = Todo.objects.all()
