from rest_framework import serializers
from .models import Tasks
from members.models import User
from django.utils import timezone


class TasksSerializer(serializers.ModelSerializer):
    assigned_to = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(),allow_null=True)

    class Meta:
        model = Tasks
        fields = [
            'id',
            'title',
            'description',
            'due_date',
            'status',
            'priority',
            'created_at',
            'updated_at',
            'created_by',
            'assigned_to',
            'tags',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at', ]

    def validate_due_date(self, value):
        """Validate that the due date is not in the past."""

        if value < timezone.now().date():
            raise serializers.ValidationError("Due date cannot be in the past.")
        return value

    def create(self, validated_data):
        #created_by=self.context['request'].user,
        task = Tasks.objects.create( **validated_data)
        return task

    # def update(self, instance, validated_data):
    #     """Update an existing task instance."""
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.description = validated_data.get('description', instance.description)
    #     instance.due_date = validated_data.get('due_date', instance.due_date)
    #     instance.status = validated_data.get('status', instance.status)
    #     instance.priority = validated_data.get('priority', instance.priority)
    #     instance.assigned_to = validated_data.get('assigned_to', instance.assigned_to)
    #     instance.tags = validated_data.get('tags', instance.tags)
    #     instance.save()
    #     return instance
