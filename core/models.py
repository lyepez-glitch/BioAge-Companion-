from django.db import models
from django.contrib.auth.models import AbstractUser,Group,Permission

# Create your models here.

class User(AbstractUser):
    # Any additional fields here

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        swappable = "AUTH_USER_MODEL"

    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_groups",  # Avoid conflict
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_permissions",  # Avoid conflict
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )


class HealthMetrics(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    height = models.FloatField()
    weight = models.FloatField()
    bmi = models.FloatField(null=True, blank=True)
    resting_heart_rate = models.FloatField(null=True, blank=True)  # New field
    hours_of_sleep = models.FloatField(null=True, blank=True)  # New field
    daily_activity_level = models.FloatField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.bmi = self.weight / (self.height / 100) ** 2
        super().save(*args, **kwargs)

class Recommendations(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recommendation_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)