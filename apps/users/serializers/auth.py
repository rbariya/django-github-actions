from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from rest_framework_simplejwt.tokens import RefreshToken


class LoginTokenSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        return super().validate(attrs)


class RefreshTokenSerializer(TokenRefreshSerializer):
    def save(self):
        refresh = self.context['request'].data.get('refresh', '')
        RefreshToken(refresh).blacklist()
