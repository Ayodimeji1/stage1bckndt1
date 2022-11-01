from django.shortcuts import render
from rest_framework import viewsets
from task1.models import TaskOne
from task1.serializers import TaskOneSerializers

# Create your views here.


class TaskOneList(viewsets.ReadOnlyModelViewSet):
    queryset = TaskOne.objects.all()
    serializer_class = TaskOneSerializers
