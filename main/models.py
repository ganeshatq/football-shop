import uuid
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('jersey', 'Jersey'),
        ('ball', 'Ball'),
        ('shoes', 'Shoes'),
        ('accessories', 'Accessories'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True) 
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    thumbnail = models.URLField(blank=True, null=True)
    products_views = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    @property
    def is_products_hot(self):
        return self.products_views > 20
        
    def increment_views(self):
        self.products_views += 1
        self.save()
    