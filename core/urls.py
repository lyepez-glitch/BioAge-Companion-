from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
from core.views import graphql

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.RegisterUserView.as_view(), name='register_user'),
    path('login/', views.LoginUserView.as_view(), name='login_user'),
    path('profile-setup/', views.ProfileSetupView.as_view(), name='profile_setup'),
    path('health-metrics/', views.HealthMetricsInputView.as_view(), name='health_metrics'),
    path('biological-age/', views.BiologicalAgeCalculationView.as_view(), name='biological_age'),
    path('recommendations/', views.RecommendationsView.as_view(), name='recommendations'),
    path('graphql/', graphql),
]
