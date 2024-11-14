from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Dish(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    dish_type = models.ForeignKey(
        "DishType", on_delete=models.CASCADE, related_name="dishes"
    )
    cooks = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="dishes")

    class Meta:
        verbose_name_plural = "dish"
    def __str__(self):
        return self.name


class DishType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Cook(AbstractUser):
    years_of_experience = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "cook"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
