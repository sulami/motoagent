from django.test import TestCase

from moto.models import Bike

class BasicBikeTestCase(TestCase):
    def test_bike_creation_and_deletion(self):
        """Test basic database interaction by creating and deleting one bike"""

        b = Bike()
        b.cylinders = 2
        b.displacement = 392
        b.engineform = 1
        b.fairings = 1
        b.ignition = 1
        b.make = 'Yamaha'
        b.model = 'XS400'
        b.power = 27
        b.seats = 2
        b.strokes = 4
        b.weight = 182
        b.year = 1981
        b.save()

        q = Bike.objects.all()
        self.assertEqual(len(q), 1)
        q = Bike.objects.filter(make='Yamaha', year__gt=1980)
        self.assertEqual(len(q), 1)

        b = q.first()

        self.assertEqual(b.displacement, 392)
        self.assertEqual(b.weight, 182)

        b.delete()

        q = Bike.objects.filter(make='Yamaha', year__gt=1980)
        self.assertEqual(len(q), 0)
        q = Bike.objects.all()
        self.assertEqual(len(q), 0)

