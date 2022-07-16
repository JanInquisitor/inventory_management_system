from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from taggit.managers import TaggableManager

# class CustomUser(AbstractUser):
#     ROLES = [
#         ('OWNER', 'owner'),
#         ('MANAGER', 'manager'),
#         ('EMPLOYEE', 'employee')
#     ]
#     # role


class Company(models.Model):
    """The company that owns and manage the storages and users."""
    name = models.CharField(max_length=50, null=False, help_text="Name of the company.")
    # owner = models.OneToOneField(User, on_delete=models.CASCADE, help_text="Owner user of the company.")


class Storage(models.Model):
    """A storage unit, can be also either a store or a factory."""
    name = models.CharField(max_length=50, null=False, help_text="Name of the storage.")
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Product(models.Model):
    """A finished product."""
    name = models.CharField(max_length=70, help_text="Name of the product.")
    price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, verbose_name="Price of the product.")
    description = models.TextField(blank=True, null=True)
    upc = models.CharField(max_length=12, help_text="Universal product code of this product.")
    quantity = models.IntegerField(default=0, verbose_name="The available quantity of the product.")
    date = models.DateTimeField(default=timezone.now)
    storage = models.ForeignKey(Storage, on_delete=models.CASCADE)
    tags = TaggableManager()

    # manufacturer

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name
