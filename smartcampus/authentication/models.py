from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    phone = models.CharField(max_length=15)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    dob = models.DateField(null=True, blank=True)
    department = models.CharField(max_length=100)
    skills = models.CharField(max_length=200)
    address = models.TextField()
    profile_picture = models.ImageField(
        upload_to='profile_pictures/',
        default='profile_pictures/default.png'
    )

    def __str__(self):
        return self.user.username