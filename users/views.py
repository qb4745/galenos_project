from django.contrib.auth.models import User, Group
from rest_framework import viewsets, status, mixins
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination


from users.serializers import (
    UserSerializer,
    UserCreateSerializer,
    GroupSerializer,
    UserDeleteSerializer,
    UserUpdateSerializer,
)


class NoPagination(PageNumberPagination):
    page_size = None  # Disable pagination


class UserListViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Endpoint de la API que permite ver usuarios.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = NoPagination  # Disable pagination for this view
    # permission_classes = [permissions.IsAuthenticated]


class UserCreateViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    Endpoint de la API que permite crear usuarios.
    """

    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    # permission_classes = [permissions.IsAuthenticated]


class UserDeleteViewSet(mixins.DestroyModelMixin, viewsets.GenericViewSet):
    """
    Endpoint de la API que permite eliminar usuarios.
    """

    queryset = User.objects.all()
    serializer_class = UserDeleteSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        user_id = instance.id  # Get the ID of the deleted user
        self.perform_destroy(instance)
        return Response(
            {"detail": f"El usuario con el Id # {user_id} ha sido eliminado."},
            status=status.HTTP_204_NO_CONTENT,
        )


class UserUpdateViewSet(mixins.UpdateModelMixin, viewsets.GenericViewSet):
    """
    Endpoint de la API que permite actualizar usuarios.
    """

    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer
    # permission_classes = [permissions.IsAuthenticated]


class RolViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Endpoint de la API que permite ver Roles.
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    pagination_class = NoPagination  # Disable pagination for this view
    # permission_classes = [permissions.IsAuthenticated]


class RolCreateViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    Endpoint de la API que permite crear Roles.
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    # permission_classes = [permissions.IsAuthenticated]


class RolDeleteViewSet(mixins.DestroyModelMixin, viewsets.GenericViewSet):
    """
    Endpoint de la API que permite eliminar Roles.
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        rol_name = instance.name  # Get the ID of the deleted user
        self.perform_destroy(instance)
        return Response(
            {"detail": f"El rol con el nombre de ' {rol_name} ' ha sido eliminado."},
            status=status.HTTP_204_NO_CONTENT,
        )


class RolUpdateViewSet(mixins.UpdateModelMixin, viewsets.GenericViewSet):
    """
    Endpoint de la API que permite actualizar Roles.
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    # permission_classes = [permissions.IsAuthenticated]
