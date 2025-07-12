from django.db import models
import uuid
from django.utils import timezone  # Import timezone

class BaseModel(models.Model):
    uid = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4, unique=True)  # Ensure uniqueness
    created_at = models.DateTimeField(auto_now_add=True, default=timezone.now)  # Add default
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
