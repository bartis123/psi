from rest_framework import serializers
from .models import Film,Klient,Pracownik,Wypozyczenie

class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields='__all__'

class KlientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Klient
        fields = '__all__'

class PracownikSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pracownik
        fields = '__all__'

class WypozyczenieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wypozyczenie
        fields = '__all__'
        
    