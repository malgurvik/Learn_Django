from django.core.management.base import BaseCommand
from faker import Faker
from lesson02_app.models import Author


faker = Faker()


class Command(BaseCommand):
    help = 'Fills the database with sample data for testing'

    def add_arguments(self, parser):
        parser.add_argument('number', type=int, help='Number of authors to create')

    def handle(self, *args, **kwargs):
        for _ in range(kwargs['number'] + 1):
            author = Author(
                first_name=faker.first_name(),
                last_name=faker.last_name(),
                email=faker.email(),
                biography=faker.text(max_nb_chars=500),
                birth_date=faker.date_of_birth(minimum_age=18, maximum_age=90)
            )
            author.save()
        self.stdout.write('Successfully created 20 authors.')
