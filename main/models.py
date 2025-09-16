from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [('fitness', 'Fitness Equipment'), ('outdoor', 'Outdoor & Camping'), ('swimming', 'Swimming Gear'), ('badminton', 'Badminton Equipment'), ('basketball', 'Basketball Gear'), ('cycling', 'Cycling'), ('yoga', 'Yoga & Pilates'), ('running', 'Running Shoes & Apparel'), ('sportswear', 'Sportswear'), ('supplements', 'Supplements & Nutrition')]
    
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES, default='sportswear')
    is_featured = models.BooleanField(default=False)
    added_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    def __str__(self):
        return self.name
