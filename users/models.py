from django.db import models
from django.contrib.auth.models import User 

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=254, null=True)

    def __str__(self):
        return self.name
        # return f'{self.user.username} Profile'

