from django.contrib.auth.models import AnonymousUser
from rest_framework_simplejwt.authentication import JWTAuthentication

class JWTAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.jwt_authenticator = JWTAuthentication()

    def __call__(self, request):
        try:
            # Authenticate the user using the JWT token in the Authorization header
            user, _ = self.jwt_authenticator.authenticate(request)
            request.user = user or AnonymousUser()
        except Exception:
            request.user = AnonymousUser()
        return self.get_response(request)

def jwt_auth_middleware(get_response):
    return JWTAuthMiddleware(get_response)
