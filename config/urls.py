from django.contrib import admin
from django.urls import path, include, re_path
from .swagger import schema_view
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include('apps.users.urls'), name='users'),
]
if settings.DEBUG:
    urlpatterns += [
        re_path(r'^api/swagger$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    ]
