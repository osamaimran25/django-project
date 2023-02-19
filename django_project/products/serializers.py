from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.Serializer):
    name = serializers.CharField(required=False)
    category = serializers.CharField(required=False)
    min_price = serializers.DecimalField(required=False, max_digits=10, decimal_places=2)
    max_price = serializers.DecimalField(required=False, max_digits=10, decimal_places=2)
    min_quantity = serializers.IntegerField(required=False)
    max_quantity = serializers.IntegerField(required=False)
    min_price = serializers.DecimalField(required=False, max_digits=10, decimal_places=2)

    def search(self):
        queryset = Product.objects.all()

        if self.validated_data.get('name'):
            queryset = queryset.filter(name__icontains=self.validated_data['name'])

        if self.validated_data.get('category'):
            queryset = queryset.filter(category__icontains=self.validated_data['category'])

        if self.validated_data.get('min_price') and self.validated_data.get('max_price'):
            queryset = queryset.filter(price__range=(self.validated_data['min_price'], self.validated_data['max_price']))
        elif self.validated_data.get('min_price'):
            queryset = queryset.filter(price__gte=self.validated_data['min_price'])
        elif self.validated_data.get('max_price'):
            queryset = queryset.filter(price__lte=self.validated_data['max_price'])

        if self.validated_data.get('min_quantity') and self.validated_data.get('max_quantity'):
            queryset = queryset.filter(quantity__range=(self.validated_data['min_quantity'], self.validated_data['max_quantity']))
        elif self.validated_data.get('min_quantity'):
            queryset = queryset.filter(quantity__gte=self.validated_data['min_quantity'])
        elif self.validated_data.get('max_quantity'):
            queryset = queryset.filter(quantity__lte=self.validated_data['max_quantity'])
        
        return queryset
