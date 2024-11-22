from django.db import models

class PeopleM(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    description = models.TextField(blank=True, null=True)  # Optional description field
    image = models.ImageField(upload_to='student_images/', blank=True, null=True)  # Optional image field
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"