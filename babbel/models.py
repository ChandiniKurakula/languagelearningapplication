from django.db import models
from django.db import models

class BabbelCode(models.Model):
    code = models.CharField(max_length=10, unique=True)
    is_valid = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.code
# Create your models here.
