from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from .models import Tasks
from .serializers import TasksSerializer


class TaskPagination(PageNumberPagination):
    page_size = 10  # Number of tasks per page


class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer
    pagination_class = TaskPagination


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer


# Create your views here.
