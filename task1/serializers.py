from rest_framework import serializers
from task1.models import TaskOne


class TaskOneSerializers(serializers.ModelSerializer):
    class Meta:
        model = TaskOne
        fields = ['slackUsername', 'backend', 'age', 'bio']

    def __init__(self, *args, **kwargs):
        super(TaskOneSerializers, self).__init__(*args, **kwargs)
