from django.core.management import BaseCommand
from django.db import connection
from main.models import Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        with connection.cursor() as cursor:
            cursor.execute("TRUNCATE TABLE main_category RESTART IDENTITY CASCADE;")

        category_list = [
            {'name': 'мясо', 'description': 'домашний скот'},
            {'name': 'рыба', 'description': 'морская, речная'},
            {'name': 'бакалея', 'description': 'крупы, макароны'},
            {'name': 'бобовые', 'description': 'горох, фасоль, нут, маш'},
            {'name': 'хлебобулочные изделия', 'description': ''},
        ]

        category_item_add = []
        for item in category_list:
            category_item_add.append(
                Category(**item)
            )

        Category.objects.bulk_create(category_item_add)