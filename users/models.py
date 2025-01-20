from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

# Create your models here.
class ProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image =models.ImageField(default='image.png', upload_to='profile', validators=[FileExtensionValidator(['png','jpg'])])
    bio = models.TextField(max_length=500, blank=True)
    
    def __str__(self):
        return self.user.username
    
    
