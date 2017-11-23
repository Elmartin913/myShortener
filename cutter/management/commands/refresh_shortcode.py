from django.core.management.base import BaseCommand, CommandError
from cutter.models import ShortURL


class Command(BaseCommand):
    help = 'Refresh all ShortURL shortcode'

    def add_arguments(self, parser):
        parser.add_argument('items', type=int)

    def handle(self, *args, **options):
        print(options)
        return ShortURL.objects.refresh_shortcode(items=options['items'])
