from django.db import models
from django.utils import timezone
from model_utils import Choices
from django.urls import reverse


class Todo(models.Model):

    STATUS = Choices("In Progress", "Completed", "Pending")

    title = models.CharField(max_length=60)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    due_date = models.DateField()
    status = models.CharField(choices=STATUS, default=STATUS.Pending, max_length=20)
    is_deleted = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("get_todo", kwargs={"id": self.id})

    def get_edit_url(self):
        return reverse("edit_todo", kwargs={"id": self.id})
