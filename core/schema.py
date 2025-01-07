import graphene
from core.models import User
from graphql_jwt.shortcuts import get_token, create_refresh_token
from .models import HealthMetrics, Recommendations


# Mutation: Register User
class RegisterUser(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        email = graphene.String(required=True)
        password = graphene.String(required=True)

    success = graphene.Boolean()
    token = graphene.String()
    refresh_token = graphene.String()

    def mutate(self, info, username, email, password):
        user = User.objects.create_user(username=username, email=email, password=password)
        token = get_token(user)
        refresh_token = create_refresh_token(user)
        return RegisterUser(success=True, token=token, refresh_token=refresh_token)


# Mutation: Login User
class LoginUser(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)

    success = graphene.Boolean()
    token = graphene.String()
    refresh_token = graphene.String()

    def mutate(self, info, username, password):
        user = User.objects.filter(username=username).first()
        if user and user.check_password(password):
            token = get_token(user)
            refresh_token = create_refresh_token(user)
            return LoginUser(success=True, token=token, refresh_token=refresh_token)
        return LoginUser(success=False, token=None, refresh_token=None)


# Mutation: Add Health Metrics
class AddHealthMetrics(graphene.Mutation):
    class Arguments:
        height = graphene.Float(required=True)
        weight = graphene.Float(required=True)
        age = graphene.Int(required=True)

    success = graphene.Boolean()

    def mutate(self, info, height, weight, age):
        user = info.context.user
        if user.is_anonymous:
            raise Exception("Authentication required!")
        HealthMetrics.objects.create(user=user, height=height, weight=weight, age=age)
        return AddHealthMetrics(success=True)


# Query: Fetch Biological Age and Recommendations
class Query(graphene.ObjectType):
    hello = graphene.String(default_value="Hello, World!")
    biological_age = graphene.Int()
    personalized_recommendations = graphene.List(graphene.String)

    def resolve_biological_age(self, info):
        user = info.context.user
        if user.is_anonymous:
            raise Exception("Authentication required!")
        health_metrics = HealthMetrics.objects.filter(user=user).first()
        if not health_metrics:
            return None
        # Example: Calculate biological age dynamically
        return health_metrics.age - 5  # Replace with your logic

    def resolve_personalized_recommendations(self, info):
        user = info.context.user
        if user.is_anonymous:
            raise Exception("Authentication required!")
        recommendations = Recommendations.objects.filter(user=user)
        return [rec.text for rec in recommendations]


# Combine All Mutations
class Mutation(graphene.ObjectType):
    register_user = RegisterUser.Field()
    login_user = LoginUser.Field()
    add_health_metrics = AddHealthMetrics.Field()


# Final Schema
schema = graphene.Schema(query=Query, mutation=Mutation)
