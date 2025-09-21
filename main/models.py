import uuid
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Shop(models.Model):
    CATEGORY_CHOICES = [
        ('kaos adidas', 'Kaos Adidas'),
        ('sepatu merah', 'Sepatu Merah'),
        ('jersey', 'Jersey'),
        ('bola', 'Bola'),
        ('sepatu futsal', 'Sepatu Futsal'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=50)
    is_featured = models.BooleanField(default=False)
    stok = models.PositiveIntegerField(default=0)
    product_views = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True) # tambahkan ini

    def __str__(self):
        return self.name
    
    @property
    def is_product_discount(self):
        return self.product_views > 20
        
    def increment_views(self):
        self.product_views += 1
        self.save()