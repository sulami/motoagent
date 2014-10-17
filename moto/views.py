from django.db.models import Q
from django.shortcuts import render

from moto.models import Bike

def table(request):

    engineform = Q()
    for i in request.GET.getlist('engineform'):
        engineform |= Q(engineform__icontains=i)
    fairings = Q()
    for i in request.GET.getlist('fairings'):
        fairings |= Q(fairings__icontains=i)
    make = Q()
    for i in request.GET.getlist('make'):
        make |= Q(make__icontains=i)
    seats = Q()
    for i in request.GET.getlist('seats'):
        seats |= Q(seats__icontains=i)

    q = Bike.objects.filter(engineform, fairings, make, seats)

    if request.GET.get('min_cylinders'):
        q.filter(cylinders__gte=request.GET.get('min_cylinders'))
    if request.GET.get('max_cylinders'):
        q.filter(cylinders__lte=request.GET.get('max_cylinders'))
    if request.GET.get('min_displacement'):
        q.filter(displacement__gte=request.GET.get('min_displacement'))
    if request.GET.get('max_displacement'):
        q.filter(displacement__lte=request.GET.get('max_displacement'))
    if request.GET.get('max_height'):
        q.filter(height__lte=request.GET.get('max_height'))
    if request.GET.get('ignition'):
        q = q.filter(ignition=request.GET.get('ignition'))
    if request.GET.get('min_power'):
        q.filter(power__gte=request.GET.get('min_power'))
    if request.GET.get('max_power'):
        q.filter(power__lte=request.GET.get('max_power'))
    if request.GET.get('min_price'):
        q.filter(price__gte=request.GET.get('min_price'))
    if request.GET.get('max_price'):
        q.filter(price__lte=request.GET.get('max_price'))
    if request.GET.get('strokes'):
        q.filter(strokes=request.GET.get('strokes'))
    if request.GET.get('min_weight'):
        q.filter(weight__gte=request.GET.get('min_weight'))
    if request.GET.get('max_weight'):
        q.filter(weight__lte=request.GET.get('max_weight'))
    if request.GET.get('min_year'):
        q.filter(year__gte=request.GET.get('min_year'))
    if request.GET.get('max_year'):
        q.filter(year__lte=request.GET.get('max_year'))

    return render(request, 'table.html', {'bikes': q})

def item(request, id):
    pass

