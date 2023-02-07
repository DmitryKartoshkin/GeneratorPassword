from django.shortcuts import render, redirect
import random
from django.core.paginator import Paginator
from generator.forms import AddSavePassword
from generator.models import Passwords
from rest_framework.viewsets import ModelViewSet
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, HttpResponseNotFound


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
    return render(request, r'generator\password.html', context)


def user_data(request):
    """Функция возвращает пароли авторизированного пользователя из БД"""
    if not request.user.is_authenticated:
        return redirect('not_registered')
    else:
        user_name = request.user
        passwords_user = Passwords.objects.filter(user=user_name)
        paginator = Paginator(passwords_user, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
            'passwords_user': passwords_user,
            'page_obj': page_obj
        }
        return render(request, r'generator\guest.html', context)


def delete(request, id):
    try:
        person = Passwords.objects.get(id=id)
        person.delete()
        return HttpResponseRedirect("/")
    except Passwords.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")


def form_save(request):
    """Функция обработки формы по сохранению в БД"""
    if request.method == 'POST':
        form = AddSavePassword(request.POST)
        if form.is_valid():
            try:
                response = form.save(commit=False)
                response.user = request.user
                form.save()
                return redirect('home')
            except:
                form.add_error(None, 'Пользователь не авторизирован')
    else:
        form = AddSavePassword()
    context = {'form': form}
    return render(request, r'generator\form_save.html', context)


def edit(request, pk):
    password = get_object_or_404(Passwords, pk=pk)
    if request.method == "POST":
        form = AddSavePassword(request.POST, instance=password)
        if form.is_valid():
            response = form.save(commit=False)
            response.user = request.user
            form.save()
            return redirect('guest')
    else:
        form = AddSavePassword(instance=password)
    context = {'form': form}
    return render(request, r'generator\edit.html', context)


