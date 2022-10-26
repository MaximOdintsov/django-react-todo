# import serializers from the REST framework
from rest_framework import serializers

# import the to_do data model
from .models import Todo


# create a serializer class
class TodoSerializer(serializers.ModelSerializer):

    # create a meta class
    class Meta:
        model = Todo
        fields = ('id', 'title', 'description', 'completed')


