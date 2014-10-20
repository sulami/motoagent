from django.db import models

form_choices = (
    (1, 'inline'),
    (2, 'v'),
    (3, 'boxer'),
    (4, 'rotary'),
    (5, 'electrical'),
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
    make = models.CharField(max_length=20)
    model = models.CharField(max_length=30)
    power = models.IntegerField(null=True)
    price = models.IntegerField(null=True)
    seats = models.IntegerField(null=True)
    strokes = models.IntegerField(null=True)
    weight = models.IntegerField(null=True)
    year = models.IntegerField()

    # TODO
    # Add variable features like electrical starters, etc...

    def __unicode__(self):
        return u'{} {} {}'.format(self.year, self.make, self.model)

    def stats(self):
        if self.cylinders:
            yield 'Engine: {} {}'.format(form_choices[self.engineform-1][1]
                                         .capitalize(), self.cylinders)
        if self.displacement:
            yield 'Displacement: {}cc'.format(self.displacement)
        if self.fairings:
            yield 'Fairings: {}'.format(fairing_choices[self.fairings-1][1]
                                        .capitalize())
        if self.height:
            yield 'Height: {}cm'.format(self.height)
        if self.ignition:
            yield 'Ignition: {}'.format(ignition_choices[self.ignition-1][1]
                                        .capitalize())
        if self.link:
            yield 'Manufacturer link: {}'.format(self.link)
        if self.make:
            yield 'Make: {}'.format(self.make)
        if self.model:
            yield 'Model: {}'.format(self.model)
        if self.power:
            yield 'Power: {}kW'.format(self.power)
        if self.price:
            yield 'Price: ${}'.format(self.price)
        if self.seats:
            yield 'Seats: {}'.format(self.seats)
        if self.strokes:
            yield 'Strokes: {}'.format(self.strokes)
        if self.weight:
            yield 'Weight: {}kg'.format(self.weight)
        if self.year:
            yield 'Release Year: {}'.format(self.year)

