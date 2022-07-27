from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    MANAGER = 1
    EMPLOYEE = 2

    # Should probably make an enum or something.
    ROLE_CHOICES = (
        (MANAGER, 'Manager'),
        (EMPLOYEE, 'Employee')
    )

    age = models.PositiveIntegerField(null=True, blank=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True)


class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
