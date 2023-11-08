from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from users import views

router = routers.DefaultRouter()
router.register(r"administracion/usuarios/gestion/crea", views.UserCreateViewSet)
router.register(r"administracion/usuarios/gestion/lista", views.UserListViewSet)
router.register(r"administracion/usuarios/gestion/elimina", views.UserDeleteViewSet)
router.register(r"administracion/usuarios/gestion/modifica", views.UserUpdateViewSet)
router.register(r"administracion/usuarios/gestion/roles", views.RolCreateViewSet)
router.register(r"administracion/usuarios/gestion/roles/lista", views.RolViewSet)
router.register(
    r"administracion/usuarios/gestion/roles/elimina", views.RolDeleteViewSet
)
router.register(
    r"administracion/usuarios/gestion/roles/modifica", views.RolUpdateViewSet
)


urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("admin/", admin.site.urls),
]
