from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(
    User, on_delete=models.CASCADE, related_name='profile')
    User._meta.get_field('email')._unique = True
    id_user = models.CharField(max_length=9,default=0 ,unique=True)
    phone = models.CharField(max_length=20)



class Medicine(models.Model):
    prescription = models.CharField(max_length=400)
    image_URL = models.CharField(max_length=400)
    price = models.FloatField(default=0)
    brand = models.CharField(max_length=30)
    description = models.CharField(max_length=400)
    medicine_name = models.CharField(default="", max_length=80)
    is_prescription = models.BooleanField(default=False)


class Products(models.Model):
    medicine_id = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    expired_date = models.DateField()


class Order_status(models.Model):
    status = models.CharField(max_length=20)


class Orders(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    order_status = models.ForeignKey(Order_status, on_delete=models.CASCADE)
    order_date = models.DateField()
    pharmacist_instruction = models.CharField(max_length=300)
    qr_code = models.ImageField(upload_to="qr_codes/" , blank=True, null=True)


class Vending_machines(models.Model):
    address = models.CharField(max_length=30)
    city = models.CharField(max_length=30)


class Inventory(models.Model):
    machine_id = models.ForeignKey(Vending_machines, on_delete=models.CASCADE)
    product_id = models.OneToOneField(Products, on_delete=models.CASCADE)


def __str__(self):
    return self.user.username


class Pharmacist_Call(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('disapproved', 'Disapproved'),
    )

    token = models.CharField(max_length=200)
    pharmacist = models.ForeignKey(User, on_delete=models.CASCADE , related_name="pharmacist" )
    patient = models.ForeignKey(User , on_delete=models.CASCADE   , default= 3)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    instructions = models.CharField(max_length=500 , default="None")
    anamnesis = models.CharField(max_length=500 , default="None")
    
