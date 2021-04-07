from django.shortcuts import render, redirect
from .models import *
from django.utils.translation import ugettext as _
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.utils.translation import activate
from django.db.models import Q
import csv
import re


def base(request):
    dragon_test = Dragon.objects.all()
    return render(request, 'Draco/base.html',
                  {
                    'title': 'ТЕСТ шапка',
                    'dragon_test': dragon_test
                  })


def main_page(request):
    return render(request, 'Draco/main_page.html',
                  {
                    'title': 'ТЕСТ',
                    'wide': True
                  })


def homes(request):
    return render(request, 'Draco/homes.html',
                  {
                    'title': 'Жилища'
                  })


def islands(request):
    return render(request, 'Draco/islands.html',
                  {
                    'title': 'Острова'
                  })


def dragons_catalog(request):
    dragons_in_catalog = Dragon.objects.all()
    return render(request, 'Draco/dragons_catalog.html',
                  {
                      'title': 'Все драконы',
                      'dragons_in_catalog': dragons_in_catalog
                  })


def draconomania_store(request):
    dragons_in_catalog = Dragon.objects.all()
    return render(request, 'Draco/draconomania_store.html',
                  {
                      'title': 'Магазин',
                      'dragons_in_catalog': dragons_in_catalog
                  })


def resource_elements(request):
    return render(request, 'Draco/resource_elements.html',
                  {
                      'title': 'Элементы'
                  })


def resource_food(request):
    return render(request, 'Draco/resource_food.html',
                  {
                      'title': 'Еда',
                  })


def resource_symbols(request):
    return render(request, 'Draco/resource_symbols.html',
                  {
                      'title': 'Символы',
                  })


def dragons(request):
    id = request.GET["id"]
    dragon = Dragon.objects.filter(id=id)[0]
    return render(request, 'Draco/dragons.html',
                  {
                      'title': 'Драконы',
                      'dragon': dragon,
                  })


from django.conf import settings


def translate(request):
    activate(request.GET["code"])
    response = HttpResponseRedirect('/')
    response.set_cookie(
        settings.LANGUAGE_COOKIE_NAME, request.GET["code"],
        max_age=settings.LANGUAGE_COOKIE_AGE,
        path=settings.LANGUAGE_COOKIE_PATH,
        domain=settings.LANGUAGE_COOKIE_DOMAIN,
        secure=settings.LANGUAGE_COOKIE_SECURE,
        httponly=settings.LANGUAGE_COOKIE_HTTPONLY,
        samesite=settings.LANGUAGE_COOKIE_SAMESITE,
    )
    return response