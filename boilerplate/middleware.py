
from datetime import timedelta
from django.utils.deprecation import MiddlewareMixin
from rest_framework_simplejwt.tokens import RefreshToken

class JwtCookieMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        if response.data.get('access'):
            access_token = response.data['access']
            refresh_token = response.data.get('refresh')
            response.set_cookie(
                'access_token',
                access_token,
                max_age=60*60,  # 1 hour
                httponly=True,
                secure=False,  # Set to True if using HTTPS
                samesite='Lax',
            )
            # if refresh_token:
            #     response.set_cookie(
            #         'refresh_token',
            #         refresh_token,
            #         max_age=60*60*24,  # 1 day
            #         httponly=True,
            #         secure=False,  # Set to True if using HTTPS
            #         samesite='Lax',
            #     )
        return response
