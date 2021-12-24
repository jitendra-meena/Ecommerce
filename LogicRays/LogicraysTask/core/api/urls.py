from django.contrib import admin
from django.urls import path
from core.api.views import *
urlpatterns = [
   path('user_update',User_Update.as_view(),name='user_update'),
   path('add_user',Add_User.as_view(),name='add_user'),
   path('order_list/<int:product_id>',Order_List.as_view(),name='order_list'),


]


