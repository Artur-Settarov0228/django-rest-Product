from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    price = models.DecimalField(max_digits=10 , decimal_places=3)
    stock = models.IntegerField()
    active = models.BooleanField(default=True)
    category = models.CharField(max_length=150)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name
    
    class Meta:
        ordering = ['-created_at']
