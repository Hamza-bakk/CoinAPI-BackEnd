from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin
from django.conf import settings
import datetime

class JwtCookieMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        if 'access' in response.data:
            access_token = response.data['access']
            expiration = datetime.datetime.now() + settings.SIMPLE_JWT["ACCESS_TOKEN_LIFETIME"]
            path = "/"
            domain=None
            secure = "False"
            httponly = True
            samsite = "None"

            # Définition du cookie
            response.set_cookie(
                key=settings.SIMPLE_JWT["AUTH_COOKIE"],
                value=access_token,
                expires=expiration,
                path=path,
                domain=domain,
                secure=False, 
                httponly=httponly,
                samesite=samsite, 
            )
            print(f"Set-Cookie: {settings.SIMPLE_JWT['AUTH_COOKIE']}={access_token}; Domain={path}; Path={path}; Expires={expiration.strftime('%a, %d %b %Y %H:%M:%S GMT')}; Secure={secure}; HttpOnly={httponly}; SameSite={samsite}")

        return response