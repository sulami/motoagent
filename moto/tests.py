from django.test import TestCase, Client

from moto.models import Bike

class UnitTestCase(TestCase):
    def setUp(self):
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

    def test_bike_creation(self):
        q = Bike.objects.all()
        self.assertEqual(len(q), 1)
        q = Bike.objects.filter(make='Yamaha', year__gt=1980)
        self.assertEqual(len(q), 1)

        b = q.first()

        self.assertEqual(b.displacement, 392)
        self.assertEqual(b.weight, 182)

    def test_bike_deletion(self):
        q = Bike.objects.all()

        b = q.first()

        self.assertEqual(b.displacement, 392)
        self.assertEqual(b.weight, 182)

        b.delete()

        q = Bike.objects.filter(make='Yamaha', year__gt=1980)
        self.assertEqual(len(q), 0)
        q = Bike.objects.all()
        self.assertEqual(len(q), 0)

class IntegrationTestCase(TestCase):
    def setUp(self):
        self.c = Client()

        b = Bike()
        b.year = 1981
        b.make = 'Yamaha'
        b.model = 'XS400'
        b.save()

        b = Bike()
        b.year = 2008
        b.make = 'Honda'
        b.model = 'CBR1000RR'
        b.save()

    def test_site_up(self):
        r = self.c.get('/')
        self.assertEqual(200, r.status_code)
        self.assertIn('<title>MotoAgent</title>', r.content)

    def test_table_with_all_bikes(self):
        r = self.c.get('/')
        self.assertEqual(200, r.status_code)
        self.assertIn('1981 Yamaha XS400', r.content)
        self.assertIn('2008 Honda CBR1000RR', r.content)

    def test_index_with_query(self):
        r = self.c.get('/?make=yamaha')
        self.assertEqual(200, r.status_code)
        self.assertIn('1981 Yamaha XS400', r.content)
        self.assertNotIn('2008 Honda CBR1000RR', r.content)

        r = self.c.get('/?min_year=2000')
        self.assertEqual(200, r.status_code)
        self.assertIn('2008 Honda CBR1000RR', r.content)
        self.assertNotIn('1981 Yamaha XS400', r.content)

    def test_query_without_results(self):
        r = self.c.get('/?make=Suzuki')
        self.assertEqual(200, r.status_code)
        self.assertNotIn('1981 Yamaha XS400', r.content)
        self.assertNotIn('2008 Honda CBR1000RR', r.content)

    def test_detail_page(self):
        r = self.c.get('/1/')
        self.assertEqual(200, r.status_code)
        self.assertIn('1981 Yamaha XS400', r.content)

        r = self.c.get('/2/')
        self.assertEqual(200, r.status_code)
        self.assertIn('2008 Honda CBR1000RR', r.content)

        r = self.c.get('/3/')
        self.assertEqual(404, r.status_code)
        self.assertNotIn('1981 Yamaha XS400', r.content)
        self.assertNotIn('2008 Honda CBR1000RR', r.content)

