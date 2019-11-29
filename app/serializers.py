from django.contrib.auth.models import User, Group
from rest_framework import serializers
from app.models import LANGUAGE_CHOICES, STYLE_CHOICES,Product,Supplier


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('productName', 'sku', 'salePrice', 'purchasePrice','vendor', 'modified_at', 'created_at')

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ( 'supplierName', 'supllierCode', 'address', 'email', 'modified_at', 'created_at')
