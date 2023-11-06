from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from users import views

router = routers.DefaultRouter()
router.register(r"administracion/usuarios/gestion/roles", views.GroupViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path(
        "administracion/usuarios/gestion/crea/",
        views.CustomUserViewSet.as_view({"post": "crea"}),
        name="user-create",
    ),
    path(
        "administracion/usuarios/gestion/lista/",
        views.CustomUserViewSet.as_view({"get": "lista"}),
        name="user-list",
    ),
    path(
        "administracion/usuarios/gestion/lista/<int:pk>/",
        views.CustomUserViewSet.as_view({"get": "detail"}),
        name="user-detail",
    ),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("admin/", admin.site.urls),
]
