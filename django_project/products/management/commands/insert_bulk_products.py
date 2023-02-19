import random
from decimal import Decimal
from django.core.management.base import BaseCommand
from products.models import Product

class Command(BaseCommand):
    help = 'Inserts 100 randomly generated Product objects into the database'

    def handle(self, *args, **options):
        if not Product.objects.all():
            for i in range(100):
                category = random.choice(['property','electronics', 'furniture', 'fashion', 'food' ])
                brand = f'Brand {i}'
                min_price = Decimal(random.randint(10, 1000))
                max_price = min_price + Decimal(random.randint(100, 500))
                min_quantity = random.randint(1, 10)
                max_quantity = min_quantity + random.randint(10, 50)

                product = Product.objects.create(
                    category=category,
                    brand=brand,
                    min_price=min_price,
                    max_price=max_price,
                    min_quantity=min_quantity,
                    max_quantity=max_quantity,
                )
                self.stdout.write(self.style.SUCCESS(f'Successfully inserted product {product}'))
        self.stdout.write(self.style.WARNING(f'Data already exist'))    