import csv
from django.core.management.base import BaseCommand
from django.utils.dateparse import parse_date
from phones.models import Phone

class Command(BaseCommand):
    help = 'Import phones from CSV file'

    def handle(self, *args, **options):
        with open('phones.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            for row in reader:
                phone, created = Phone.objects.update_or_create(
                    id=row['id'],
                    defaults={
                        'name': row['name'],
                        'image': row['image'],
                        'price': row['price'],
                        'release_date': parse_date(row['release_date']),
                        'lte_exists': row['lte_exists'].lower() in ('true', '1', 'yes'),
                    }
                )
                action = 'Created' if created else 'Updated'
                self.stdout.write(self.style.SUCCESS(f'{action} phone {phone.name}'))
