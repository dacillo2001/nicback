from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()  # Fetch all tasks
    serializer_class = TaskSerializer  # Serialize the task data
