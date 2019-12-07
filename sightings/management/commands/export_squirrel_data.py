from django.core.management.base import BaseCommand, CommandError
from sightings.models import Squirrel
import csv
import datetime

class Command(BaseCommand):
    help = 'A command that can be used to export the squirrel data to a given path'

    def get_model_fields(model):
        return model._meta.fields

    def add_arguments(self, parser):
        parser.add_argument('path', type=str, help='/path/to/file.csv')
    def handle(self, *args, **options):
        path = options['path']
        fields = Squirrel._meta.fields
        with open(path, 'w') as csvfile:
            writer = csv.writer(csvfile)
            # write your header first
            for obj in Squirrel.objects.all():
                row = ""
                for field in fields:
                    if isinstance(getattr(obj,field.name),bool):
                        if getattr(obj, field.name) == True:
                            row += 'TRUE' + ","
                        elif getattr(obj, field.name) == False:
                            row += 'FALSE' + ","
                    elif isinstance(getattr(obj,field.name),int) or isinstance(getattr(obj,field.name),float):
                        row += str(getattr(obj, field.name)) + ","
                    elif isinstance(getattr(obj,field.name),datetime.date):
                        row += getattr(obj,field.name).strftime("%m%d%Y")
                    else:
                        row += getattr(obj,field.name)
                writer.writerow(row)
        self.stdout.write(self.style.SUCCESS('Successfully export data to %s' % path))
