from rest_framework import viewsets
from rest_framework import viewsets, permissions

from .models import Task
from .serializers import TaskSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=['get'])
    def in_progress(self, request):
        tasks = Task.objects.filter(status='in_progress')
        serializer = self.get_serializer(tasks, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def completed(self, request):
        tasks = Task.objects.filter(status='completed')
        serializer = self.get_serializer(tasks, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def overdue(self, request):
        tasks = Task.objects.filter(status='overdue')
        serializer = self.get_serializer(tasks, many=True)
        return Response(serializer.data)
