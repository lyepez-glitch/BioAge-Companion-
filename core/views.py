from django.shortcuts import render

from rest_framework import status, views
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.tokens import RefreshToken
from .models import HealthMetrics
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
from .models import Recommendations
from graphql_jwt.middleware import JSONWebTokenMiddleware
User = get_user_model()

from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView

@csrf_exempt
def graphql(request, *args, **kwargs):
    view = GraphQLView.as_view(graphiql=True, middleware=[JSONWebTokenMiddleware()])
    return view(request, *args, **kwargs)

class LoginUserView(TokenObtainPairView):
    """
    View for logging in users and generating JWT tokens.
    """
    pass
class RegisterUserView(views.APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        # Check if user already exists
        if User.objects.filter(username=data["username"]).exists():
            return Response({"error": "Username already exists!"}, status=status.HTTP_400_BAD_REQUEST)

        # Create new user
        user = User.objects.create(
            username=data["username"],
            email=data["email"],
            password=make_password(data["password"]),
        )

        # Create JWT token for the user
        refresh = RefreshToken.for_user(user)
        return Response({
            "access_token": str(refresh.access_token),
            "refresh_token": str(refresh),
        }, status=status.HTTP_201_CREATED)

class ProfileSetupView(views.APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = request.user
        data = request.data

        # Use update_or_create to handle both creation and updates
        health_metrics, created = HealthMetrics.objects.update_or_create(
            user=user,
            defaults={
                "height": data.get("height"),
                "weight": data.get("weight"),
            }
        )

        if created:
            message = "Profile setup successful!"
        else:
            message = "Profile updated successfully!"

        return Response({"message": message}, status=status.HTTP_200_OK)

class HealthMetricsInputView(views.APIView):
    def post(self, request, *args, **kwargs):
        user = request.user
        data = request.data

        ## Update or create health metrics for the user
        health_metrics, created = HealthMetrics.objects.update_or_create(
            user=user,
            defaults={
                "resting_heart_rate": data["resting_heart_rate"],
                "hours_of_sleep": data["hours_of_sleep"],
                "daily_activity_level": data["daily_activity_level"],
            }
        )

        return Response({"message": "Health metrics updated!"}, status=status.HTTP_200_OK)


class BiologicalAgeCalculationView(views.APIView):
    def get(self, request, *args, **kwargs):
        return Response({"message": "This is a GET response"})


    def post(self, request, *args, **kwargs):
        user = request.user
        health_metrics = HealthMetrics.objects.get(user=user)

        # Simplified biological age calculation (custom formula)
        biological_age = health_metrics.height * 0.1 + health_metrics.weight * 0.2 + health_metrics.resting_heart_rate * 0.3
        if biological_age < 30:
            rec_text = "You're in great shape! Keep up the good work with your health metrics."
        elif 30 <= biological_age < 50:
            rec_text = "Your biological age is healthy, but consider increasing your daily activity level."
        elif biological_age >= 50:
            rec_text = "Consider working on reducing your resting heart rate and improving sleep for better health."
        else:
            rec_text = "No specific recommendations based on the current data."

        Recommendations.objects.create(user=user, recommendation_text=rec_text)
        return Response({"biological_age": biological_age,"recommendation": rec_text}, status=status.HTTP_200_OK)


class RecommendationsView(views.APIView):
    def get(self, request, *args, **kwargs):
        user = request.user
        recommendations = Recommendations.objects.filter(user=user)
        return Response({"recommendations": [rec.recommendation_text for rec in recommendations]}, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        user = request.user
        rec_text = request.data["recommendation_text"]
        recommendation = Recommendations.objects.create(user=user, recommendation_text=rec_text)
        return Response({"recommendation": rec_text}, status=status.HTTP_201_CREATED)

