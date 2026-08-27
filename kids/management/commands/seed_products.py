from datetime import datetime, timezone

from django.core.management.base import BaseCommand

from kids.models import Product


PRODUCTS = [
    ("Rainbow Cloud Tee", "T-Shirt", 16, "Girls - 3-7 Yrs", "9.svg"),
    ("Ocean Explorer Set", "Set", 28, "Boys - 4-8 Yrs", "10.svg"),
    ("Meadow Bunny Dress", "Dress", 26, "Girls - 2-6 Yrs", "11.svg"),
    ("Little Skater Joggers", "Joggers", 22, "Unisex - 3-8 Yrs", "12.svg"),
    ("Sunshine Cotton Shorts", "Shorts", 18, "Boys - 2-6 Yrs", "13.svg"),
    ("Daisy Day Cardigan", "Cardigan", 32, "Girls - 4-10 Yrs", "14.svg"),
    ("Cozy Bear Sleep Set", "Sleepwear", 24, "Baby - 6-24 Mos", "15.svg"),
    ("Sailboat Summer Romper", "Romper", 29, "Baby - 0-18 Mos", "16.svg"),
]


class Command(BaseCommand):
    help = "Add the sample kids-fashion products and their local images."

    def handle(self, *args, **options):
        created = 0
        updated = 0
        product_date = datetime(2026, 8, 27, 15, 30, tzinfo=timezone.utc)

        for name, category, price, description, image_name in PRODUCTS:
            product, was_created = Product.objects.update_or_create(
                Products_name=name,
                defaults={
                    "category": category,
                    "price": price,
                    "des": description,
                    "date": product_date,
                    "image": f"kids/images/{image_name}",
                },
            )
            if was_created:
                created += 1
            else:
                updated += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Seeded {len(PRODUCTS)} products ({created} created, {updated} updated)."
            )
        )
