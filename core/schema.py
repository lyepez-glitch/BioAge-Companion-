import graphene
from graphene_django.types import DjangoObjectType
from .models import HealthMetrics,Recommendations

# Define the HealthMetricsType to expose the HealthMetrics model through GraphQL
class HealthMetricsType(DjangoObjectType):
    class Meta:
        model = HealthMetrics

class RecommendationsType(DjangoObjectType):
    class Meta:
        model = Recommendations

# Query to get health metrics for the logged-in user
class Query(graphene.ObjectType):
    health_metrics = graphene.Field(HealthMetricsType)
    recommendations = graphene.List(RecommendationsType)

    def resolve_health_metrics(self, info):
        user = info.context.user
        if user.is_anonymous:
            raise Exception("Authentication required")
        health_metrics = HealthMetrics.objects.filter(user=user).first()
        if health_metrics:
            return health_metrics
        return None
    def resolve_recommendations(self, info):
        user = info.context.user
        if user.is_anonymous:
            raise Exception("Authentication required")
        # Fetch recommendations for the logged-in user
        recommendations = Recommendations.objects.filter(user=user)
        return recommendations

class UpdateHealthMetrics(graphene.Mutation):
    class Arguments:
        resting_heart_rate = graphene.Float()  # Only include the fields being updated in the mutation
        hours_of_sleep = graphene.Float()
        daily_activity_level = graphene.Float()

    success = graphene.Boolean()

    def mutate(self, info, resting_heart_rate, hours_of_sleep, daily_activity_level):
        user = info.context.user
        print('user info' + str(user) + ' info ' + str(info.context))
        # if user.is_anonymous:
        #     raise Exception("Authentication required")

        # Update the health metrics for the user
        health_metrics, created = HealthMetrics.objects.update_or_create(
            user=user,
            defaults={
                "resting_heart_rate": resting_heart_rate,
                "hours_of_sleep": hours_of_sleep,
                "daily_activity_level": daily_activity_level
            }
        )

        return UpdateHealthMetrics(success=True)

class Mutation(graphene.ObjectType):
    update_health_metrics = UpdateHealthMetrics.Field()


# Define the schema to include both Query and Mutation
schema = graphene.Schema(query=Query, mutation=Mutation)


