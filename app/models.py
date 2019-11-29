from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from .utils import TimeStampable

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])

class Supplier(TimeStampable, models.Model):
    supplierName=models.CharField(max_length=60)
    supllierCode=models.CharField(max_length=10)
    address=models.CharField(max_length=100)
    email=models.EmailField(max_length=50)
    def __str__(self):
        return self.supplierName

class Product(TimeStampable, models.Model):
    productName=models.CharField(max_length=60)
    sku=models.CharField(max_length=10)
    salePrice=models.DecimalField(max_digits=8, decimal_places=2, null=True)
    purchasePrice=models.DecimalField(max_digits=8, decimal_places=2, null=True)
    vendor=models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='products')
