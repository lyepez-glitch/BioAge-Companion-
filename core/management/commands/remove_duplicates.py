from django.core.management.base import BaseCommand
from django.db import models
from core.models import HealthMetrics

class Command(BaseCommand):
    help = 'Remove duplicate HealthMetrics records'

    def handle(self, *args, **kwargs):
        duplicates = (
            HealthMetrics.objects
            .values('user')  # Group by user
            .annotate(count=models.Count('id'))  # Count instances per user
            .filter(count__gt=1)  # Keep only users with more than 1 record
        )

        for duplicate in duplicates:
            user_id = duplicate['user']
            health_metrics = HealthMetrics.objects.filter(user_id=user_id).order_by('id')
            # Keep the first record and delete the rest
            health_metrics.exclude(id=health_metrics.first().id).delete()

        self.stdout.write(self.style.SUCCESS('Duplicate HealthMetrics records removed!'))
