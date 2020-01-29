from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.http import Http404
# Create your views here.
@api_view(['GET','POST'])
def klient_list(request):
    if request.method == 'GET':
        klient1 = Klient.objects.all()
        serializer = KlientSerializer(klient1, many=True)
        #return JsonResponse(serializer.data, safe=False)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = KlientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            #return JsonResponse (serializer.data, status.HTTP_201_CREATED)
            return Response(serializer.data, status.HTTP_201_CREATED)
        #return JsonResponse(serializer.data, status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def klient_detail(request, pk):
    try:
        klient1 = Klient.objects.get(pk=pk)
    except Klient.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = KlientSerializer(klient1)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = KlientSerializer(klient1, request.data)
        if serializer.is_valid():
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.data, status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        Klient.delete()
        return Response(status.HTTP_204_NO_CONTENT)

@api_view(['GET','POST'])
def pracownik_list(request):
    if request.method == 'GET':
        pracownik1 = Pracownik.objects.all()
        serializer = PracownikSerializer(pracownik1, many=True)
        #return JsonResponse(serializer.data, safe=False)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = PracownikSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            #return JsonResponse (serializer.data, status.HTTP_201_CREATED)
            return Response(serializer.data, status.HTTP_201_CREATED)
        #return JsonResponse(serializer.data, status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def pracownik_detail(request, pk):
    try:
        pracownik1 = Pracownik.objects.get(pk=pk)
    except Pracownik.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = PracownikSerializer(pracownik1)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = PracownikSerializer(pracownik1, request.data)
        if serializer.is_valid():
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.data, status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        Pracownik.delete()
        return Response(status.HTTP_204_NO_CONTENT)

@api_view(['GET','POST'])
def film_list(request):
    if request.method == 'GET':
        film1 = Film.objects.all()
        serializer = FilmSerializer(film1, many=True)
        #return JsonResponse(serializer.data, safe=False)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = FilmSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            #return JsonResponse (serializer.data, status.HTTP_201_CREATED)
            return Response(serializer.data, status.HTTP_201_CREATED)
        #return JsonResponse(serializer.data, status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def film_detail(request, pk):
    try:
        film1 = Film.objects.get(pk=pk)
    except Film.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = FilmSerializer(film1)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = FilmSerializer(film1, request.data)
        if serializer.is_valid():
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.data, status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        Film.delete()
        return Response(status.HTTP_204_NO_CONTENT)

@api_view(['GET','POST'])
def wypozyczenie_list(request):
    if request.method == 'GET':
        wypozyczenie1 = Wypozyczenie.objects.all()
        serializer = WypozyczenieSerializer(wypozyczenie1, many=True)
        #return JsonResponse(serializer.data, safe=False)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = WypozyczenieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            #return JsonResponse(serializer.data, status.HTTP_201_CREATED)
            return Response(serializer.data, status.HTTP_201_CREATED)
        #return JsonResponse(serializer.data, status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def wypozyczenie_detail(request, pk):
    try :
       wypozyczenie1 = Wypozyczenie.objects.get(pk=pk)
    except wypozyczenie1.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = WypozyczenieSerializer(wypozyczenie1)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = WypozyczenieSerializer(wypozyczenie1, request.data)
        if serializer.is_valid():
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.data, status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        Wypozyczenie.delete()
        return Response(status.HTTP_204_NO_CONTENT)