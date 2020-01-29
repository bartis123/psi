from django.urls import path
from . import views

urlpatterns = [
    path('klienci', views.klient_list),
    path('klient/<int:pk>', views.klient_detail),
    path('pracownicy', views.pracownik_list),
    path('pracownik/<int:pk>', views.pracownik_detail),
    path('filmy', views.film_list),
    path('film/<int:pk>', views.film_detail),
    path('wypozyczenia', views.wypozyczenie_list),
    path('wypozyczenie/<int:pk>', views.wypozyczenie_detail),
]


