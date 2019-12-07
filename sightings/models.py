from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class Squirrel(models.Model):
    longitude = models.FloatField('Longitude')

    latitude = models.FloatField('Latitude')

    squirrel_id = models.CharField(help_text = _('Unique Squirrel ID'),
        max_length=50,
        primary_key=True)


    AM = 'AM'
    PM = 'PM'

    shift = models.CharField(
        help_text=_('Shift'),
        max_length=2,
        choices =((AM,'AM'),(PM,'PM'),),
        default=AM,
    )

    date = models.DateField('Date')

    ADULT = 'Adult'
    JUVENILE = 'Juvenile'
    UNKNOWN = 'Unknown'

    age = models.CharField(
            help_text = _('Age'),
            max_length = 50,
            choices = ((ADULT,'Adult'),(JUVENILE,'Juvenile'),(UNKNOWN,'Unknown'),),
            default = UNKNOWN,
            )
    
    GRAY = 'Gray'
    CINNAMON = 'Cinnamon'
    BLACK = 'Black'

    COLOR_CHOICES = (
        (GRAY, 'Gray'),
        (CINNAMON, 'Cinnamon'),
        (BLACK, 'Black'),
        (UNKNOWN, 'Unknown'),
    )

    color = models.CharField(
        help_text=_('Primary Fur Color'),
        max_length=50,
        choices=COLOR_CHOICES,
        default=UNKNOWN,
    )


    GROUND_PLANE = 'Ground Plane'
    ABOVE_GROUND = 'Above Ground'

    LOCATION_CHOICES = (
        (GROUND_PLANE, 'Ground Plane'),
        (ABOVE_GROUND, 'Above Ground'),
        (UNKNOWN, 'Unknown'),
    )

    location = models.CharField(
        help_text=_('Location'),
        max_length=50,
        choices=LOCATION_CHOICES,
        default=UNKNOWN,
    )

    specific_location = models.CharField(
        help_text=_('Specific Location'),
        max_length=100,
        default = UNKNOWN,
    )

    running = models.BooleanField(
        help_text = _('Running'),
        default=False,
    )

    chasing = models.BooleanField(
        help_text = _('Chasing'),
        default=False,
    )

    climbing = models.BooleanField(
        help_text = _('Climbing'),
        default=False,
    )

    eating = models.BooleanField(
        help_text = _('Eating'),
        default=False,
    )

    foraging = models.BooleanField(
        help_text = _('Foraging'),
        default=False,
    )

    other_activities = models.CharField(
        help_text = _('Other Activities'),
        max_length=100,
        default = UNKNOWN,
    )

    kuks = models.BooleanField(
        help_text = _('Kuks'),
        default=False,
    )

    quaas = models.BooleanField(
        help_text = _('Quaas'),
        default=False,
    )

    moans = models.BooleanField(
        help_text = _('Moans'),
        default=False,
    )

    tail_flags = models.BooleanField(
        help_text = _('Tail Flags'),
        default=False,
    )

    tail_twitches = models.BooleanField(
        help_text = _('Tail Twitches'),
        default=False,
    )

    approaches = models.BooleanField(
        help_text = _('Approaches'),
        default=False,
    )

    indifferent = models.BooleanField(
        help_text = _('Indifferent'),
        default=False,
    )

    runs_from = models.BooleanField(
        help_text = _('Runs From'),
        default=False,
    )

    def __str__(self):
        return self.squirrel_id



