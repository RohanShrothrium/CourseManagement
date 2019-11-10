from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    DepName = models.CharField(max_length=10, default='')
    Cpi = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    def __str__(self):
        return f'{self.user.username} Profile'