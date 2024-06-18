from django.db import models
from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    
    def get_course_info(self):
        """Method to return course information."""
        return {
            'title': self.title,
            'description': self.description,
            # Add more fields as needed
        }
# Create your models here.
