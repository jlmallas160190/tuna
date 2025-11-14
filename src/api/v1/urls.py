from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .login.views import LoginView
from .medical_appointments.views import MedicalSpecialityViewSet
from .users.views import UserCreateView, UserDetailView, UserListView

router = DefaultRouter()
router.register(
    r"medical-specialities", MedicalSpecialityViewSet, basename="speciality"
)

urlpatterns = [
    path("", include(router.urls)),
    path("login/", LoginView.as_view(), name="auth"),
    path("register/", UserCreateView.as_view(), name="user-register"),
    path("users", UserListView.as_view(), name="user-list"),
    path("users/<int:pk>/", UserDetailView.as_view(), name="user-detail"),
]
