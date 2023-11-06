from django.contrib.auth.models import User, Group
from rest_framework import viewsets, status
from rest_framework import permissions
from rest_framework.response import Response
from users.serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Hash the password before saving the user
        user = serializer.save()
        user.set_password(request.data.get("password"))
        user.save()

        headers = self.get_success_headers(serializer.data)
        response_data = serializer.data
        response_data[
            "url"
        ] = "http://127.0.0.1:8000/administracion/usuarios/gestion/users/crea/"

        return Response(response_data, status=status.HTTP_201_CREATED, headers=headers)


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
