from django.urls import path
from .views import MyTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView
from . import views
from .views import RegisterApi
urlpatterns = [
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/', views.get_profile),
    path('register/', RegisterApi.as_view()),

]