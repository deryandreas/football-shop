from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    descriptipn = models.TextField()
    thumbnail = models.URLField()
    category = models.CharField(max_length=50)
    is_featured = models.BooleanField()

    def __str__(self):
        return self.name