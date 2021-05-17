from django.urls import path, include

from rest_framework.routers import SimpleRouter

from apps.users.views import UserViewSet
from apps.users.views.auth import LoginView, LogoutView

router = SimpleRouter(trailing_slash=False)
router.register('users', UserViewSet, basename="users")

# urlpatterns = router.urls
urlpatterns = [
    path('auth/login', LoginView.as_view(), name="login"),
    path('auth/logout', LogoutView.as_view(), name='logout'),
    path('', include(router.urls)),
]
