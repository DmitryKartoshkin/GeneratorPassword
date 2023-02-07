from django.urls import path

from registration.views import LoginUser, logout_user, RegisterUser, not_registered

urlpatterns = [
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('registration/', RegisterUser.as_view(), name='registration'),
    path('notregistered/', not_registered, name='not_registered')
]