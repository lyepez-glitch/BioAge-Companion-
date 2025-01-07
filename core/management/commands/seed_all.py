from django.core.management.base import BaseCommand
import random

class Command(BaseCommand):
    help = 'Seeds the database with initial data for User, HealthMetrics, and Recommendations'

    def handle(self, *args, **kwargs):
        # Import models inside the handle method to avoid circular import
        from core.models import User, HealthMetrics, Recommendations

        # Seed Users
        users = []
        for i in range(5):  # Create 5 users as an example
            user = User.objects.create_user(
                username=f'user{i}',
                email=f'user{i}@example.com',
                password='password123'
            )
            users.append(user)
            self.stdout.write(self.style.SUCCESS(f'Created user: {user.username}'))

        # Seed Health Metrics for each user
        for user in users:
            height = random.uniform(150, 190)  # Random height in cm
            weight = random.uniform(45, 100)  # Random weight in kg
            health_metrics = HealthMetrics.objects.create(
                user=user,
                height=height,
                weight=weight
            )
            health_metrics.save()
            self.stdout.write(self.style.SUCCESS(f'Created health metrics for user: {user.username}'))

        # Seed Recommendations for each user
        recommendations = [
            'Eat a balanced diet',
            'Exercise regularly',
            'Drink plenty of water',
            'Get enough sleep',
            'Manage stress effectively',
        ]

        for user in users:
            for rec_text in recommendations:
                recommendation = Recommendations.objects.create(
                    user=user,
                    recommendation_text=rec_text
                )
                recommendation.save()
                self.stdout.write(self.style.SUCCESS(f'Created recommendation for user: {user.username}'))

        self.stdout.write(self.style.SUCCESS('Successfully seeded all data!'))
