from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('home/', views.home, name='home'),
    
    path('restaurants/', views.restaurants, name='restaurants'),
    path('menu/<str:restaurant_name>/', views.view_menu, name='view_menu'),
    path('green-bowl/', views.green_bowl),
    path('chocolate-room/', views.chocolate_room),
    path('kfc/', views.kfc),
    path('pizza/', views.pizza),
    path('burger/', views.burger, name='burger'),
    path('meals/', views.meals, name='meals'),
    path('paradise/', views.paradise, name='paradise'),
    path('feedback/', views.feedback, name='feedback'),
    path('feedback-success/',
     views.feedback_success,
     name='feedback_success'),
    path('cart/', views.cart, name='cart'),
    path('add-to-cart/', views.add_to_cart, name='add_to_cart'),
    path('payment/', views.payment, name='payment'),
    path('tracking/', views.tracking, name='tracking'),
    path('success/', views.success, name='success'),
]