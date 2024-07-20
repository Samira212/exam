from django.urls import path
from .views import *


urlpatterns = [
    path('userprofile/', UserProfileViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='userprofile_list'),

    path('userprofile/<int:pk>/', CategoryViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='user_profile_detail'),




    path('food/', FoodViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='food_list'),

    path('food/<int:pk>/', FoodViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='food_detail'),

    path('Courier/', CourierViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='courier_list'),

    path('order/<int:pk>/', OrderViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='order_detail'),

    path('Delivery/', DeliveryViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='delivery_list'),

    path('delivery/<int:pk>/', DeliveryViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='delivery_detail'),


    path('rating/', RatingViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='rating_list'),

    path('rating/<int:pk>/', RatingViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='rating_detail'),


path('Review/', ReviewViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='review_list'),

path('Review/<int:pk>/', ReviewViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='review_detail'),



]



