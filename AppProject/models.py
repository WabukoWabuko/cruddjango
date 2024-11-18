from django.db import models

# Create your models here.
class TestUserCrud(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    # image = models.ImageField() 
    
    def __str__(self):
        return self.name