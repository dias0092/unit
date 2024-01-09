import uuid
from django.db import models

# Create your models here.
class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.username