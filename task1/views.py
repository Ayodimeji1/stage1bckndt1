from django.shortcuts import render
from rest_framework import viewsets
from task1.models import TaskOne
from task1.serializers import TaskOneSerializers
from django.http import JsonResponse

# Create your views here.


# class TaskOneList(viewsets.ReadOnlyModelViewSet):
#     queryset = TaskOne.objects.all()
#     serializer_class = TaskOneSerializers


def taskoneView(request):
    taskone = {
        'slackUsername':'ayodimejia1',
        'backend':True,
        'age': 33,
        'bio': 'self-taught backend developer',
        }

    return JsonResponse(taskone)
