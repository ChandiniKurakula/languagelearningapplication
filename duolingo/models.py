from django.db import models
from django.contrib.auth.models import User
from django.db import models
class Duolingo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    def _str_(self):
        return self.title
    
    


# Create your models here.
