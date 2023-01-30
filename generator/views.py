from django.shortcuts import render, redirect
import random

from generator.forms import AddSavePassword
from generator.models import Passwords


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
    context = {'passwords_user': passwords_user}
    return render(request, 'generator\guest.html', context)


def form_save(request):
    """Функция обработки формы по сохранению в БД"""
    if request.method == 'POST':
        form = AddSavePassword(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('home')
            except:
                form.add_eror(None, 'Ошибка')
    else:
        form = AddSavePassword()
    context = {'form': form}
    return render(request, 'generator\\form_save.html', context)

