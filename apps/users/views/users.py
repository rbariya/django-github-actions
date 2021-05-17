from rest_framework import views
from rest_framework.response import Response
from rest_framework import viewsets, mixins

from apps.users.models import User
from apps.users.serializers import UserSerializer, UserBasicSerializer


class AccountProfileView(views.APIView):
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return Response(self.serializer_class(request.user).data)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class UserViewSet(mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    queryset = User.objects.filter(is_deleted=False)
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        '''
        Create Admin User only
        '''
        self.serializer_class = UserBasicSerializer
        response = super().create(request, *args, **kwargs)
        response.data = {
            "message": "Admin User created",
            "data": response.data
        }
        return response

    def perform_create(self, serializer):
        serializer.save(is_admin=True)

    def destroy(self, request, *args, **kwargs):
        user = self.get_object()
        user.soft_delete()
        return Response({"message": "User Deleted Successfully"})
