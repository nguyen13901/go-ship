
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls import url
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from drf_yasg import openapi
from drf_yasg.views import get_schema_view as swagger_get_schema_view
from rest_framework import permissions
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from rest_framework import routers

from api_user.views.user import UserViewSet

schema_view = swagger_get_schema_view(
    openapi.Info(
        title="GoShipAPI",
        default_version='1.0.0',
        description="API documentation of GoShipAPI",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    patterns=[
        path(r'api/v1/users', include("api_user.urls")),
    ]
)
urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'api/v1/users/', include("api_user.urls")),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
