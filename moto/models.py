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

class Bike(models.Model):
    cylinders = models.IntegerField()
    displacement = models.IntegerField()
    engineform = models.IntegerField(choices=form_choices)
    fairings = models.IntegerField(choices=fairing_choices)
    height = models.IntegerField()
    make = models.CharField(max_length=20)
    model = models.CharField(max_length=30)
    power = models.IntegerField()
    price = models.IntegerField()
    release = models.IntegerField()
    seats = models.IntegerField()
    weight = models.IntegerField()

