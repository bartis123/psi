from django.db import models

# Create your models here.
class Film (models.Model):
    title = models.CharField(max_length=200)
    rezyser =models.CharField(max_length=200)
    gatunek =models.CharField(max_length=200)
    opis =models.CharField(max_length=500)
    cena = models.IntegerField()

class Klient(models.Model):
    imie = models.CharField(max_length=200)
    nazwisko = models.CharField(max_length=200)
    mail = models.CharField(max_length=200)
    telefon =models.IntegerField()

class Pracownik(models.Model):
    imie = models.CharField(max_length=200)
    nazwisko = models.CharField(max_length=200)

class Wypozyczenie(models.Model):
    idFilm = models.ForeignKey(Film, on_delete=models.CASCADE)
    idKlient = models.ForeignKey(Klient, on_delete=models.CASCADE)
    idPracownik = models.ForeignKey(Pracownik, on_delete=models.CASCADE)
    dataWypozyczenia =models.DateField()
    dataZwrotu = models.DateField()


