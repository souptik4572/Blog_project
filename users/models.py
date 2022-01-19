from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


# Creating a custom user class for storing all the users who can also sign in using their email
class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), max_length=250, unique=True)


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    # For using our CustomUser model we need to pass additional arguments
    def save(self, *args, **kwargs):
        super().save()
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
