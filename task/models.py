from django.db import models
from members.models import User
from django.contrib.postgres.fields import ArrayField


class Tasks(models.Model):
    STATUS = (
        ('pending', 'Pending'),
        ('in-progress', 'In-Progress'),
        ('completed', 'Completed')
    )
    PRIORITY = (
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High')
    )
    title = models.CharField(max_length=80)
    description = models.TextField()
    due_date = models.DateField()
    status = models.CharField(choices=STATUS, default='pending', max_length=20)
    priority = models.CharField(choices=PRIORITY, default='medium', max_length=20)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="created_tasks")
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name="assigned_tasks", null=True)
    tags = ArrayField(models.CharField(max_length=50), blank=True, null=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.title
# Create your models here.
