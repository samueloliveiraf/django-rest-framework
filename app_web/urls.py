from django.contrib import admin
from django.urls import path
from accounts.views import (
    UserListCreateAPIView,
    ProfileListCreateAPIView
)

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('list-user/', UserListCreateAPIView.as_view()),
    path('list-profiles/', ProfileListCreateAPIView.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
