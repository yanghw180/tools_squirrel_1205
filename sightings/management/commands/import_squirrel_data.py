from django.core.management.base import BaseCommand, CommandError
from sightings.models import Squirrel
import csv
import datetime

# reference: https://docs.djangoproject.com/en/2.2/howto/custom-management-commands/
class Command(BaseCommand):
    help = 'A command that can be used to import the data from a given path'
    def bool(self, b):
        if b.lower() == "true":
            return True
        else:
            return False

    def add_arguments(self, parser):
        parser.add_argument('path',help='/path/to/file.csv',type=str)

    def handle(self, *args, **options):
        path = options['path']
        # reference: https://stackoverflow.com/questions/2459979/how-to-import-csv-data-into-django-models
        with open(path) as f:
            reader = csv.DictReader(f)
            data = list(reader)

            for item in data:
                _, created = Squirrel.objects.get_or_create(
                    longitude = float(item['X']),
                    latitude = float(item['Y']),
                    squirrel_id = item['Unique Squirrel ID'],
                    shift = item['Shift'],
                    date = datetime.date(int(item['Date'][-4:]),int(item['Date'][:2]),int(item['Date'][2:4])),
                    age = item['Age'],
                    color = item['Primary Fur Color'],
                    location = item['Location'],
                    specific_location = item['Specific Location'],
                    running = self.bool(item['Running']),

                    chasing = self.bool(item['Chasing']),
                    climbing = self.bool(item['Climbing']),
                    eating = self.bool(item['Eating']),
                    foraging = self.bool(item['Foraging']),
                    other_activities = item['Other Activities'],
                    kuks = self.bool(item['Kuks']),
                
                    quaas = self.bool(item['Quaas']),
                    moans = self.bool(item['Moans']),
                    tail_flags = self.bool(item['Tail flags']),
                    tail_twitches = self.bool(item['Tail twitches']),
                    approaches = self.bool(item['Approaches']),
                    indifferent = self.bool(item['Indifferent']),
                    runs_from = self.bool(item['Runs from']),
                )
            # creates a tuple of the new object or
            # current object and a boolean of if it was created


        self.stdout.write(self.style.SUCCESS('Successfully import data from "%s"' % path))
