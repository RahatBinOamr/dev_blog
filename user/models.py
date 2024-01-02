from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=50, choices=GENDER, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=13, blank=True, null=True)
    image = models.ImageField(upload_to='Profile_image', default='Profile_image/default.png')


    class Meta:

        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        
        return f'{self.user.username} Profile'