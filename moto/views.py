from django.db.models import Q
from django.shortcuts import render

from moto.models import Bike

def index(request):
    pass

def table(request):
    q = Bike.objects.filter(
        # TODO multiple choice queries

        cylinders__gte=request.GET['min_cylinders'],
        cylinders__lte=request.GET['max_cylinders'],
        displacement__gte=request.GET['min_displacement'],
        displacement__lte=request.GET['max_displacement'],

        engineform = models.IntegerField(choices=form_choices, null=True)
        fairings = models.IntegerField(choices=fairing_choices, null=True)

        height__lte=request.GET['max_height'],
        ignition=request.GET['ignition'],

        make__icontains=request.GET['make'],

        power__gte=request.GET['min_power'],
        power__lte=request.GET['max_power'],
        price__gte=request.GET['min_price'],
        price__lte=request.GET['max_price'],

        seats = models.IntegerField(null=True)

        strokes=request.GET['strokes'],
        weight__gte=request.GET['min_weight'],
        weight__lte=request.GET['max_weight'],
        year__gte=request.GET['min_year'],
        year__lte=request.GET['max_year'],
    )

def item(request, id):
    pass

