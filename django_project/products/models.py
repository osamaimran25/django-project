from django.db import models

class Product(models.Model):
    category = models.CharField(max_length=255, null=True, blank=True)
    brand = models.CharField(max_length=255,  null=True, blank=True)
    min_price = models.DecimalField(max_digits=8, decimal_places=2,  null=True, blank=True)
    max_price = models.DecimalField(max_digits=8, decimal_places=2,  null=True, blank=True)
    min_quantity = models.IntegerField( null=True, blank=True)
    max_quantity = models.IntegerField( null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    max_price = models.DecimalField(max_digits=8, decimal_places=2,  null=True, blank=True)
