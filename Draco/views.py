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
    main_pages = MainPageTranslation.objects.filter(language=request.LANGUAGE_CODE)
    return render(request, 'Draco/main_page.html',
                  {
                    'title': 'Главная страница',
                    'main_pages': main_pages,
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
    dragons_in_catalog = DragonTranslation.objects.filter(language=request.LANGUAGE_CODE)
    return render(request, 'Draco/dragons_catalog.html',
                  {
                      'title': 'Все драконы',
                      'dragons_in_catalog': dragons_in_catalog,
                  })


def dragon_list(request):
    search_query = request.GET.get('search', '')

    if search_query:
        dragon_trans = DragonTranslation.objects.filter(Q(name__icontains=search_query) |
                                                        Q(rarity__icontains=search_query))
    else:
        dragon_trans = DragonTranslation.objects.filter(language=request.LANGUAGE_CODE)
    return render(request, 'Draco/dragons_catalog.html', {'search_query': search_query, 'dragons': dragon_trans})


def dragons(request):
    id = request.GET["id"]
    dragon = Dragon.objects.filter(id=id)[0]
    dragon_trans = DragonTranslation.objects.filter(dragon=dragon, language=request.LANGUAGE_CODE)[0]
    return render(request, 'Draco/dragons.html',
                  {
                      'title': 'Драконы',
                      'dragon': dragon,
                      'dragon_trans': dragon_trans,
                  })


def draconomania_store(request):
    dragons_in_catalog = DragonTranslation.objects.filter(language=request.LANGUAGE_CODE)
    return render(request, 'Draco/draconomania_store.html',
                  {
                      'title': 'Магазин',
                      'dragons_in_catalog': dragons_in_catalog
                  })


def order(request):
    orders = Orders(
        username=request.POST['username'],
        phone=request.POST['phone'],
        product_id=request.POST['product_id'],
        )
    orders.save()
    return redirect('/store')


def resource_elements(request):
    elements = ElementsTranslation.objects.filter(language=request.LANGUAGE_CODE)
    elements_compare = TheStrengthWeaknessTranslation.objects.filter(language=request.LANGUAGE_CODE)
    return render(request, 'Draco/resource_elements.html',
                  {
                      'title': 'Элементы',
                      'elements': elements,
                      'elements_compare': elements_compare,
                      'wide': True
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


def calculator(request):
    dragons = DragonTranslation.objects.filter(language=request.LANGUAGE_CODE)
    return render(request, 'Draco/base.html', {'title': 'Калькулятор', 'dragons': dragons})


def do_calculator(request):
    calculator = CalculatorDragons.objects.filter(dragon1=request.POST['choose1'], dragon2=request.POST['choose2'])
    return render(request, 'Draco/base.html',
                  {'title': 'Результаты', 'calculator': calculator[0], 'wide': True})


def register(request):
    user = User.objects.create_user(
        request.POST['username'],
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        password=request.POST['password'],
        email=request.POST['email']
    )
    client = Client(user=user, address='Минск')
    client.save()
    return redirect('/register_done')


def see_register(request):
    return render(request, 'Draco/register.html', {'title': 'Регистрация'})


def register_done(request):
    new_user = User.objects.filter()
    return render(request, 'Draco/register_done.html', {'title': 'Регистрация завершена', 'new_user': new_user})


def login_user(request):
    user = authenticate(
        username=request.POST['username'],
        password=request.POST['password'],
    )
    if user is None:
        return render(request, 'Draco/error.html')
    else:
        login(request, user)
        return HttpResponseRedirect('/')


def do_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect('/')
    else:
        return HttpResponse('Вы не залогинены')


def see_login(request):
    return render(request, 'Draco/login.html', {'title': 'Войти|Выйти'})


def error(request):
    return render(request, 'Draco/error.html', {'title': 'Ошибка входа'})




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


def server(request):
    User.objects.filter(
        id=request.PUT['id']
    ).update(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        password=request.POST['password'],
        email=request.POST['email']
    )
    return JsonResponse({'status': 'OK'})


def get_csv(request):
    responce = HttpResponse(content_type='text/csv')
    responce['Content-Disposition'] = "attachment; filename=dragons.csv"

    writer = csv.writer(responce)
    writer.writerow(['id', 'name', 'rarity', 'description1', 'description2', 'description3', 'description4'])
    dragontrans = DragonTranslation.objects.all()
    for el in dragontrans:
        writer.writerow([el.id, el.name, el.rarity, el.description1])
    return responce
