from django.urls import path

from generator.views import home, password, user_data, form_save, delete, edit

urlpatterns = [
    path('', home, name='home'),
    path('password/', password, name='password'),
    path('guest/', user_data, name='guest'),
    path('save/', form_save, name='save'),
    path("guest/delete/<int:id>/", delete, name='delete'),
    path("guest/edit/<int:pk>/", edit, name='edit'),

]
