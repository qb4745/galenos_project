from django.contrib.auth.models import User, Group
from rest_framework import viewsets, status
from rest_framework import permissions
from rest_framework.response import Response
from users.serializers import UserSerializer, GroupSerializer
from rest_framework import generics
from rest_framework.decorators import action
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist


class CustomUserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer

    @action(detail=False, methods=["post"])
    def crea(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Hash the password before saving the user
        user = serializer.save()
        user.set_password(request.data.get("password"))
        user.save()

        headers = self.get_success_headers(serializer.data)
        response_data = serializer.data
        return Response(response_data, status=status.HTTP_201_CREATED, headers=headers)

    @action(detail=False, methods=["get"])
    def lista(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=["get"])
    def detail(self, request, pk):
        user = User.objects.get(pk=pk)
        serializer = self.get_serializer(user)
        return Response(serializer.data)


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
