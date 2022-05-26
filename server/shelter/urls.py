from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('admin/', admin.site.urls),
    path('api/', include('session_api.urls', namespace='session_api')),
    path('api/user/', include('users.urls', namespace='users')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include('sesh.urls', namespace='sesh')),
    path('docs/', include_docs_urls(title='SessionAPI')),
    path('schema', get_schema_view(
        title='SessionAPI',
        description='API for the SessionAPI',
        version='1.0.0'
    ), name='openapi-schema')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
