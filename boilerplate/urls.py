from django.contrib import admin
from django.urls import include, path
from graphene_django.views import GraphQLView
from alerts.schema import schema as alerts_schema

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),
    path("graphql", GraphQLView.as_view(graphiql=True, schema=alerts_schema)),
]
