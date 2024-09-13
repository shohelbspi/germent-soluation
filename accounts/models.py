from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save


# Create your models here.

from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    user_type_choices = (
        ('1', "Admin"),
        ('2', "Planning"),
        ('3', "Yarn Store"),
        ('4', "Fabric Store"),
        ('5', "Floor")
    )
    user_type = models.CharField(max_length=120, choices=user_type_choices, default='1')


class Profile(models.Model):
    auth_user_id = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    mobile_number = models.CharField(max_length=20)
    designation = models.CharField(max_length=50)  
    department = models.CharField(max_length=50)  
    employee_id = models.CharField(max_length=50)
    profile_pic = models.FileField(upload_to='profile_pics/', null=True, blank=True)  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)


@receiver(post_save, sender=User)
def create_or_save_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(auth_user_id=instance)
    else:
        instance.profile.save()
