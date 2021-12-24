from users.models import User 
from rest_framework import serializers
from core.models import Product, Order

class User_UpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','first_name','last_name','email','phone','password','profile_pic']



class Add_UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','first_name','last_name','email','phone','password','profile_pic']


class Product_ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class Order_ListSerializer(serializers.ModelSerializer):
    product = Product_ListSerializer(many = True)
    class Meta:
        model = Order
        fields = '__all__'
