from django.shortcuts import render
from rest_framework import viewsets
from api_app.models import List
from api_app.serializers import ListSerializer



class ListViewSet(viewsets.ModelViewSet):
    queryset= List.objects.all()
    serializer_class = ListSerializer