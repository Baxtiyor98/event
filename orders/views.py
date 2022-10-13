import json

from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import (DevicesService, SnacksService, Order, Quantity, Place)
from .utils import send_email
import datetime


def index(request):
    for i in Order.objects.filter(is_deleted=False):
        if (i.date-datetime.datetime.now().date()).days < 0:
            i.is_deleted = True
    return render(request, 'calendar.html', context={"snacks": SnacksService.objects.all(),
                                                     "devices": DevicesService.objects.all(),
                                                     "places": Place.objects.all(),
                                                     "orders":Order.objects.filter(is_active=True, is_deleted=False).order_by("date","start_time")})


def get_order(request):
    if request.method == 'POST':
        place = Place.objects.get(id=int(request.POST.get('place')))
        order = Order.objects.create(fullname=request.POST["fullname"],
                                     company=request.POST["company"],
                                     position=request.POST["lavozim"],
                                     email=request.POST["email"],
                                     phone=request.POST["phone"],
                                     start_time=request.POST["start_time"],
                                     finish_time=request.POST["finish_time"],
                                     place=place,
                                     people=int(request.POST["people"]),
                                     date=datetime.datetime.strptime(request.POST.get("date_data"), "%d %b %Y"))
        if request.POST["file"]:
            order.file = request.POST["file"]
            order.save()
        for i in request.POST.getlist("device"):
            if i:
                order.device.add(int(i))
        for j in request.POST.getlist("snack"):
            if j:
                Quantity.objects.create(order=order, snack_id=int(j), number=int(request.POST["quantity" + j]))
        send_email({'to_email': order.email,
                    'code': f"{order.fullname}, Ваш запрос будет получен в ближайшее время."})
        return redirect('index')


def admin(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        message = request.POST.get('message')
        order = Order.objects.get(id=int(id))
        send_email({'to_email': order.email,
                    'code': f"{message}"})
        order.delete()
        return redirect('admin')
    return render(request, 'admin.html',{"orders":Order.objects.filter(is_active=False,is_deleted=False).order_by('id'),
                                         'quantity':Quantity.objects.all()})


def accept(request):
    data = json.load(request)
    order = Order.objects.get(id=int(data["id"]))
    order.is_active = True
    order.save()
    send_email({'to_email': order.email,
               'code': f"{order.fullname}, Ваш запрос был получен в ближайшее время."})
    return JsonResponse({"message":'Ok'})
