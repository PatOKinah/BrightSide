import time
import json
import urllib
import urllib.request
import requests
import sys
from geopy.geocoders import Nominatim

ulica = input("Podaj ulicę: ")
miasto = input("Podaj miasto: ")

geolokalizator = Nominatim()

lokalizacja = geolokalizator.geocode(ulica + " " + miasto)
szerokoscGeo = lokalizacja.latitude
dlugoscGeo = lokalizacja.longitude
print(lokalizacja.address)
print("Szerokość geograficzna: "+ str(szerokoscGeo))
print("Długość geograficzna: " + str(dlugoscGeo))

urlgeo = str("http://api.openweathermap.org/data/2.5/weather?lat="+str(szerokoscGeo)+"&lon="+str(dlugoscGeo)+"&appid=HERE_YOU MUST_TYPE_YOURS_ID_CODE&lang=pl&units=metric")

#odczytanie pliku json zawartego pod linkiem urlgeo
plikjson = urllib.request.urlopen(urlgeo)
jsonstring = plikjson.read()
parsuj_json = json.loads(jsonstring)
#zapis danych z pliku JSON do odpowiednich zmiennych
pogoda = parsuj_json["weather"][0]["main"]
pogodaPL = parsuj_json["weather"][0]["description"]
zachmurzenie = parsuj_json["clouds"]["all"]
cisnienie = parsuj_json["main"]["pressure"]
temperatura = parsuj_json["main"]["temp"]
temperaturaMin= parsuj_json["main"]["temp_min"]
temperaturaMax = parsuj_json["main"]["temp_max"]
wilgotnosc = parsuj_json["main"]["humidity"]
wiatrPredkosc = parsuj_json["wind"]["speed"]
wiatrKierunek = parsuj_json["wind"]["deg"]
wschodSlonca = parsuj_json["sys"]["sunrise"]
zachodSlonca = parsuj_json["sys"]["sunset"]

print("Pogoda: " + pogoda)
print("Pogoda: " + pogodaPL)
print("Zachmurzenie: " + str(zachmurzenie) + "%")
print("Ciśnienie: " + str(cisnienie) + "hPa")
print("Temperatura: " + str(temperatura) + " C")
print("Temperatura minimalna: " + str(temperaturaMin) + " C")
print("Temperatura maksymalna: " + str(temperaturaMax) + " C")
print("Wilgotność względna: " + str(wilgotnosc) + "%")
print("Prędkość wiatru: " + str(wiatrPredkosc) + "km/h")
print("Kierunek wiatru: " + str(wiatrKierunek) + " stopni" )
print("Wschód Słońca: " + time.ctime(wschodSlonca))
print("Zachód Słońca: " + time.ctime(zachodSlonca))