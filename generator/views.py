from django.shortcuts import render, redirect
import random

from generator.forms import AddSavePassword
from generator.models import Password


menu = [
        {'title': "Добавить статью"},
        {'title': "Обратная связь"},
        {'title': "Войти", 'url_name': 'login'}
]


def home(request):
    context = {'menu': menu}
    return render(request, 'generator\home.html', context)


def password(request):
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
    passwords_user = Password.objects.all()
    context = {'passwords_user': passwords_user}
    return render(request, 'generator\guest.html', context)


def form_save(request):
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

