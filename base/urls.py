from django.urls import path

from . import views

urlpatterns = [
    path('signup/', views.RegisterAPI.as_view(), name="api-signup"),
    path('login/', views.LoginAPI.as_view(), name='api-login'),
    path('logout/', views.LogoutAPI.as_view(), name="api-logout"),
]
