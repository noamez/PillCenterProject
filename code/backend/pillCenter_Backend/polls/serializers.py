from rest_framework import serializers
from polls.models import *
from rest_framework import  serializers
from django.contrib.auth.models import User ,Group 
from django_email_verification import send_email
from .models import Orders , Order_status , Pharmacist_Call
from django.core.files import File
from .mailOrder import send_mail_order
from io import BytesIO
import datetime
import qrcode


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['phone','id_user'] 

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create(**validated_data)
        Profile.objects.create(**profile_data, user=user)
        return user



class RegisterSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    class Meta:
        model = User 
        fields = ('username','password','first_name','last_name','email','profile')
        extra_kwargs = {
            'password':{'write_only': True},
        }
    def create(self, validated_data ):
        profile_data = validated_data.pop('profile')
        user = User.objects.create_user(validated_data['username'],     password = validated_data['password']  ,    first_name=validated_data['first_name']  ,    last_name=validated_data['last_name'] ,    email=validated_data['email']  )
        Profile.objects.create(**profile_data, user=user)
       # user.is_active = False
        group = Group.objects.get(name='patient') 
        group.user_set.add(user)
        send_email(user)
        return user



class OrderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order_status
        fields = '__all__'


class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    medicine_id = MedicineSerializer()
    class Meta:
        model = Products
        fields = '__all__'

class OrdersSerializer(serializers.ModelSerializer):
    user_id = UserSerializer()
    product_id = ProductSerializer()
    order_status = OrderStatusSerializer()
    class Meta:
        model = Orders
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Orders
        fields = ['user_id' ,'product_id' , 'pharmacist_instruction']

    def create(self,validated_data):

        order = Orders.objects.create(user_id =validated_data['user_id'] ,product_id = validated_data['product_id'],pharmacist_instruction= validated_data['pharmacist_instruction'] , order_status_id = 1 ,
        order_date = datetime.datetime.now())
        qr = qrcode.QRCode(version=None, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
        qr.add_data("OR" + str(order.id))
        qr.add_data("PR" + str(order.product_id.id))
        qr.add_data("CL" + str(order.user_id.id))
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        blob = BytesIO()
        img_file = img.save(blob, 'JPEG')  
        order.qr_code.save('qr.jpg', File(blob), save=True)
        user =validated_data['user_id']
        
        send_mail_order(order=order,user=user)
        return order 

class Pharmacist_Call_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Pharmacist_Call
        fields = [ "id",'token' , 'pharmacist']
    def create(self, validated_data):
        obj = Pharmacist_Call.objects.create(**validated_data)

        return obj

class Pharmacist_Call_BasicSerializers(serializers.ModelSerializer):
    class Meta:
        model = Pharmacist_Call
        fields = '__all__'