from django.contrib import admin
from django.urls import path, include  # `include` is used to include app-specific URLs
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('graphql',csrf_exempt(GraphQLView.as_view(graphiql=True))),  # If you're using GraphQL
    path('api/', include('core.urls')),  # Including URLs from the `myapp` app
]
