from django.db import models

form_choices = (
    (1, 'inline'),
    (2, 'v'),
    (3, 'boxer'),
    (4, 'rotary'),
)

fairing_choices = (
    (1, 'naked'),
    (2, 'bikini'),
    (3, 'half'),
    (4, 'full'),
)

ignition_choices = (
    (1, 'carbureted'),
    (2, 'fuel injected'),
)

class Bike(models.Model):
    cylinders = models.IntegerField(null=True)
    displacement = models.IntegerField(null=True)
    engineform = models.IntegerField(choices=form_choices, null=True)
    fairings = models.IntegerField(choices=fairing_choices, null=True)
    height = models.IntegerField(null=True)
    ignition = models.IntegerField(choices=ignition_choices, null=True)
    link = models.URLField(null=True)
    make = models.CharField(max_length=20, null=True)
    model = models.CharField(max_length=30, null=True)
    power = models.IntegerField(null=True)
    price = models.IntegerField(null=True)
    seats = models.IntegerField(null=True)
    strokes = models.IntegerField(null=True)
    weight = models.IntegerField(null=True)
    year = models.IntegerField(null=True)

    # TODO
    # Add variable features like electrical starters, etc...

    def __unicode__(self):
        return u'{} {} {}'.format(self.release, self.make, self.model)

