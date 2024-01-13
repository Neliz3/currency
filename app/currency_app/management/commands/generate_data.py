from django.core.management.base import BaseCommand
from currency_app.models import Rate, ContactUs
import random


def generate_rate(number_of_records):
    for i in range(number_of_records):
        Rate.objects.create(
            currency=random.choice(('usd', 'eur')),
            sale=random.randint(2000, 2999)/100,
            buy=random.randint(2000, 2999)/100,
            source=random.choice(('monobank', 'privatbank'))
        )


def generate_contact(number_of_records):
    for i in range(number_of_records):
        ContactUs.objects.create(
            email_from='',
            subject='',
            message=''
        )


class Command(BaseCommand):
    help = "Generate Random Data"

    def add_arguments(self, parser):

        # Positional argument
        parser.add_argument(
            'model',
            type=str,
            help='Indicates the Model'
        )

        # Optional argument
        parser.add_argument(
            '--records',
            type=int,
            default=10,
            help='Indicates the number of records to be created'
        )

    def handle(self, *args, **options):

        model = options['model']
        number_of_records = options['records']

        if model in ('Rate', 'rate'):
            generate_rate(number_of_records)

        elif model in ('ContactUs', 'contactus'):
            generate_contact(number_of_records)

        else:
            print('Invalid model')
