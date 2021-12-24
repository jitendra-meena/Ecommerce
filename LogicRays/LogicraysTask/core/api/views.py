from rest_framework.generics import CreateAPIView, ListCreateAPIView, ListAPIView
from users.models import User 
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .serializers import User_UpdateSerializer, Add_UserSerializer, Order_ListSerializer
from core.models import Product, Order

class User_Update(ListAPIView):
    queryset = User.objects.all()
    serializer_class = User_UpdateSerializer
    def get(self,request):
        user_obj = User.objects.filter(is_active = True,is_superuser = False)
        serializer = User_UpdateSerializer(user_obj,many = True)
        return Response({'status':'200','msg':'success','data':serializer.data})


class Add_User(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = Add_UserSerializer
    def get(self,request):
        user_obj = User.objects.filter(is_active = True,is_superuser = False)
        serializer = Add_UserSerializer(user_obj)
        return Response({'status':'200','msg':'success','data':serializer.data})
    def post(self,request):
        first_name = request.data.get('user.first_name','')
        last_name = request.data.get('user.last_name','')
        email = request.data.get('user.email','')
        phone = request.data.get('user.phone','')
        password = request.data.get('user.password','')
        image = request.data.get('profile_pic')
      
        user_exs =  User.objects.filter(email = email,is_active = True).exists()
        if user_exs:
            return Response({'msg':'Email already taken'})
        user_exs = User.objects.filter(phone = phone, is_active = True).exists() 
        if user_exs:
            return Response({'msg':'Phone number already taken'})
        else:
            user = User.objects.create_user(email = email, phone = phone, password= password, first_name = first_name, last_name = last_name,profile_pic = image, is_active = True) 
        user_obj = User.objects.get(id = user.id)
        serializer = Add_UserSerializer(user_obj)
        return Response({'status':'200' ,'msg': 'Successfully Update Data', 'data':serializer.data})          


class Order_List(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = Order_ListSerializer
    def get(self,request,product_id):
        product_obj = Order.objects.get(id = product_id)
        serializer = Order_ListSerializer(product_obj)
        return Response({'status':'200','msg':'success','data':serializer.data})

        