from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("", views.index, name="index"),
    path('menu/', views.MenuItemView.as_view(), name="menuItem"),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view(), name="menuItem"),
    path('api-token-auth/', obtain_auth_token),
]