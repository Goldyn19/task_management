from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from .models import Tasks
from members.models import User
from .serializers import TasksSerializer


class TasksAPITestCase(APITestCase):

    def setUp(self):
        # Create users for assigning tasks
        self.user1 = User.objects.create_user(username="user1", email="user1@example.com", password="password123")
        self.user2 = User.objects.create_user(username="user2", email="user2@example.com", password="password123")
        self.user3 = User.objects.create_user(username="user3", email="user3@example.com", password="password123")

        # Data for creating a new task
        self.task_data = {
            "title": "Test Task",
            "description": "This is a test task.",
            "due_date": "2024-11-30",
            "status": "pending",
            "priority": "medium",
            "assigned_to": self.user2.id,
            "tags": ["urgent", "work"],
            "created_by": self.user1.id
        }

    def test_create_task(self):
        url = reverse('task-list-create')
        self.client.force_authenticate(user=self.user1)
        response = self.client.post(url, self.task_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Tasks.objects.count(), 1)
        self.assertEqual(Tasks.objects.get().title, "Test Task")

    def test_retrieve_all_tasks(self):
        # Create a sample task
        self.client.force_authenticate(user=self.user1)
        task_serializer = TasksSerializer(data=self.task_data)
        if task_serializer.is_valid():
            task_serializer.save()  # Save the task to the database

        url = reverse('task-list-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)  # With pagination, tasks are in `results` key

    def test_retrieve_task_by_id(self):
        # Create a sample task
        self.client.force_authenticate(user=self.user1)
        task_serializer = TasksSerializer(data=self.task_data)
        if task_serializer.is_valid():
            task = task_serializer.save()  # Save the task to the database

        url = reverse('task-detail', args=[task.id])  # Accessing the task's ID
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Test Task")

    def test_update_task(self):
        # Create a sample task
        self.client.force_authenticate(user=self.user1)
        task_serializer = TasksSerializer(data=self.task_data)
        if task_serializer.is_valid():
            task = task_serializer.save()  # Save the task to the database

        url = reverse('task-detail', args=[task.id])
        updated_data = {
            "title": "Updated Task Title",
            "description": "Updated task description",
            "due_date": "2024-12-01",
            "status": "in-progress",
            "priority": "high",
            "assigned_to": self.user3.id,
            "tags": ["important", "client"],
            "created_by": self.user1.id
        }
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        task.refresh_from_db()  # Refresh the instance from the database
        self.assertEqual(task.title, "Updated Task Title")
        self.assertEqual(task.status, "in-progress")

    def test_delete_task(self):
        # Create a sample task
        self.client.force_authenticate(user=self.user1)
        task_serializer = TasksSerializer(data=self.task_data)
        if task_serializer.is_valid():
            task = task_serializer.save()  # Save the task to the database

        url = reverse('task-detail', args=[task.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Tasks.objects.count(), 0)
