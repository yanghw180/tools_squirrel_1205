from django.core.management.base import BaseCommand, CommandError
from sightings.models import Squirrel
import csv
import datetime

class Command(BaseCommand):
    help = 'A command that can be used to export the squirrel data to a given path'

    def add_arguments(self, parser):
        parser.add_argument('path', type=str, help='/path/to/file.csv')

    # reference:https://stackoverflow.com/questions/15029666/exporting-items-from-a-model-to-csv-django-python
    def handle(self, *args, **options):
        path = options['path']
        fields = Squirrel._meta.fields
        with open(path, 'w') as csvfile:
            writer = csv.writer(csvfile)
            # write your header first
            row = []
            for field in fields:
                if field.name.lower() == 'squirrel_id':
                    row.append('Unique Squirrel ID')
                else:
                    row.append(field.name.title())
            writer.writerow(row)

            for obj in Squirrel.objects.all():
                row = []
                for field in fields:
                    if isinstance(getattr(obj,field.name),bool):
                        if getattr(obj, field.name) == True:
                            row.append('TRUE')
                        elif getattr(obj, field.name) == False:
                            row.append( 'FALSE' )
                    elif isinstance(getattr(obj,field.name),int) or isinstance(getattr(obj,field.name),float):
                        row.append( str(getattr(obj, field.name)) )
                    elif isinstance(getattr(obj,field.name),datetime.date):
                        row.append( getattr(obj,field.name).strftime("%m%d%Y") )
                    else:
                        row.append( getattr(obj,field.name) )
                writer.writerow(row)
        self.stdout.write(self.style.SUCCESS('Successfully export data to %s' % path))
