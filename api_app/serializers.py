from rest_framework import serializers
from .models import List

class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = ['list_id', 'list_name']
