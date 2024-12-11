from django.core.management.base import BaseCommand

from HikingTrails.Hikers.models import Hiker


class Command(BaseCommand):
    help = 'Fill Hiker table with is_approved users'

    def handle(self, *args, **kwargs):
        approved_hikers = Hiker.objects.filter(is_approved=True)
        for hiker in approved_hikers:
            hiker, created = Hiker.objects.get_or_create(
                username=hiker.username,
                defaults={
                    'first_name': hiker.first_name,
                    'last_name': hiker.last_name,
                    'email': hiker.email,
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Hiker {hiker.username} created'))
            else:
                self.stdout.write(self.style.WARNING(f'Hiker {hiker.username} already exists'))
