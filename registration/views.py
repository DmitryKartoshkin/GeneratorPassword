from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from registration.forms import RegisterUserForm
from django.contrib.auth import logout, login


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'registration\\registration.html'
    success_url = reverse_lazy('login')
    #
    # def form_valid(self, form):
    #     user = form.save()
    #     login(self.reqest, user)
    #     return redirect('guest')


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'registration\login.html'

    def get_success_url(self):
        return reverse_lazy('guest')


def logout_user(request):
    logout(request)
    return redirect('login')




