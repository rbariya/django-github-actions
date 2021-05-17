from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_401_UNAUTHORIZED
from rest_framework_simplejwt.exceptions import TokenError

from apps.users.models import User
from apps.users.serializers.auth import LoginTokenSerializer, RefreshTokenSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class LoginView(TokenObtainPairView):
    serializer_class = LoginTokenSerializer

    def post(self, request, *args, **kwargs):
        print(request.data)
        if not User.objects.filter(email=request.data['email'], is_deleted=False).exists():
            return Response({'message': "No active account found with the given credentials"},
                            status=HTTP_401_UNAUTHORIZED)
        try:
            return super().post(request, *args, **kwargs)

        except Exception:
            return Response({'message': 'No active account found with the given credentials.'},
                            status=HTTP_401_UNAUTHORIZED)


class LogoutView(GenericAPIView):
    serializer_class = RefreshTokenSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        except TokenError:
            pass
        return Response({'detail': 'Successfully logged out.'})
