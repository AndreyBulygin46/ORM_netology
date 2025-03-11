from django.http import Http404
from django.shortcuts import render

from main.models import Car, Sale


def cars_list_view(request):
    # получите список авто
    template_name = 'main/list.html'
    cars = Car.objects.all()
    return render(request, template_name, {'cars':cars})  # передайте необходимый контекст


def car_details_view(request, car_id):
    # получите авто, если же его нет, выбросьте ошибку 404
    try:
        car = Car.objects.get(pk=car_id)
    except Car.DoesNotExist:
        raise Http404('Car not found')
    else:
        template_name = 'main/details.html'
        return render(request, template_name, {'car':car})  # передайте необходимый контекст


def sales_by_car(request, car_id):
    try:
        car   = Car.objects.get(pk=car_id)
        sales = Sale.objects.filter(car=car)
        template_name = 'main/sales.html'
        return render(request, template_name, {'car': car, 'sales': sales})
    except Car.DoesNotExist:
        raise Http404('Car not found')