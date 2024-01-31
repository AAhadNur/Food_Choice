from django.urls import path

from . import views

urlpatterns = [
    path('signup/', views.RegisterAPI.as_view(), name="signup"),
    path('login/', views.LoginAPI.as_view(), name='login'),
    path('logout/', views.LogoutAPI.as_view(), name="logout"),

    path('restaurants/', views.RestaurantListCreateAPIView.as_view(),
         name="restaurant-list-create"),
    path('restaurants/<int:pk>/', views.RestaurantDetailUpdateDeleteAPIView.as_view(),
         name='restaurant-detail-update-delete'),

    path('menus/', views.MenuListCreateAPIView.as_view(), name='menu-list-create'),
    path('menus/<int:pk>/', views.MenuDetailUpdateDeleteAPIView.as_view(),
         name='menu-detail-update-delete'),
    path('menus/current-day/', views.CurrentDayMenuAPIView.as_view(),
         name='current-day-menu'),

]
