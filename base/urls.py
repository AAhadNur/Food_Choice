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

    path('vote-create/', views.VoteCreateAPIView.as_view(), name='vote-create'),

    path('feedbacks/', views.FeedbackListAPIView.as_view(), name='feedback-list'),
    path('feedbacks/create/', views.FeedbackCreateAPIView.as_view(),
         name='feedback-create'),

    path('daily-results/', views.DailyResultsListAPIView.as_view(),
         name='daily-results-list'),
    path('daily-results/create/', views.DailyResultsCreateAPIView.as_view(),
         name='daily-results-create'),
    path('daily-results/current-date/', views.DailyResultsCurrentDateAPIView.as_view(),
         name='daily-results-current-date'),

]
