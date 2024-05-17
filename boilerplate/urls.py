from django.contrib import admin
from django.urls import include, path
from graphene_django.views import GraphQLView
from alerts.schema import schema as alerts_schema
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),
    path("graphql", csrf_exempt(GraphQLView.as_view(graphiql=True, schema=alerts_schema))),
]
