from django.contrib.auth.models import User
from django.db import models

UserTypeChoice = [
    (0, 'Student'),
    (1, 'Instructor'),
    (2, 'Administrator'),
]


class Profile(models.Model):
    user = models.OneToOneField(User, models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    DeptName = models.CharField(max_length=50)
    Cpi = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    UserType = models.IntegerField(choices=UserTypeChoice)

    def __str__(self):
        return f'{self.user.username} ({self.user.first_name} {self.user.last_name})'
