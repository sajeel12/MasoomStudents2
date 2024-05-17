from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('rooms/', views.getRooms),
    path('rooms/<str:pk>/', views.getRoom),
    path('key/', views.getKey),  # Adding new URL pattern
    path('one-app-jazzcash-key/', views.oneAppJazzCashKey),  # Adding new URL pattern
]