from django.urls import path
from . import views

urlpatterns = [
    path('', views.TaskListCreateView.as_view(), name='task-list-create'),  # POST and GET /tasks
    path('<int:pk>', views.TaskDetailView.as_view(), name='task-detail'),   # GET, PUT, DELETE /tasks/:id
]
