from django.shortcuts import render, redirect
import random
from django.core.paginator import Paginator
from generator.forms import AddSavePassword
from generator.models import Passwords
from rest_framework.viewsets import ModelViewSet


def home(request):
    # context = {'menu': menu}
    return render(request, 'generator\home.html')


def password(request):
    """Функция генерирует пароль"""
    characters = list('abcdefghijklnmopqrstuvwxyz')
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))
    lenght = int(request.GET.get('length', 8))
    the_password = ''
    for i in range(lenght):
        the_password += random.choice(characters)
    context = {'password': the_password}
    return render(request, 'generator\password.html', context)


def user_data(request):
    # passwords_user = Passwords.objects.all()
    """Функция возвращает пароли авторизированного пользователя из БД"""
    user_name = request.user
    passwords_user = Passwords.objects.filter(user=user_name)
    paginator = Paginator(passwords_user, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'passwords_user': passwords_user,
        'page_obj': page_obj
    }
    return render(request, 'generator\guest.html', context)


def dell_password(request):
    print(request.GET)

    return render(request, 'generator\dell.html')


def form_save(request):
    """Функция обработки формы по сохранению в БД"""
    if request.method == 'POST':
        form = AddSavePassword(request.POST)
        if form.is_valid():
            try:
                response = form.save(commit=False)
                print(response.user)
                print(request.user)
                response.user = request.user
                form.save()
                return redirect('home')
            except:
                form.add_eror(None, 'Ошибка')
    else:
        form = AddSavePassword()
    context = {'form': form}
    return render(request, 'generator\\form_save.html', context)

