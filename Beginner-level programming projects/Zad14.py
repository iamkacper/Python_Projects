""" Obliczanie pola figury:
Program, który oblicza pole prostokąta, trójkąta lub koła na podstawie danych podanych przez użytkownika. """

import math

def pole_prostokata(dlugosc, szerokosc):
    """Oblicza pole prostokąta."""
    return dlugosc * szerokosc

def pole_trojkata(podstawa, wysokosc):
    """Oblicza pole trójkąta."""
    return (podstawa * wysokosc) / 2

def pole_kola(promien):
    """Oblicza pole koła."""
    return math.pi * promien ** 2

def wybierz_figure():
    """Funkcja umożliwiająca wybór figury i obliczenie jej pola."""
    print("Wybierz figurę:")
    print("1. Prostokąt")
    print("2. Trójkąt")
    print("3. Koło")

    wybor = input("Podaj numer figury (1/2/3): ")

    if wybor == "1":
        dlugosc = float(input("Podaj długość prostokąta: "))
        szerokosc = float(input("Podaj szerokość prostokąta: "))
        pole = pole_prostokata(dlugosc, szerokosc)
        print(f"Pole prostokąta wynosi: {pole} jednostek kwadratowych.")

    elif wybor == "2":
        podstawa = float(input("Podaj długość podstawy trójkąta: "))
        wysokosc = float(input("Podaj wysokość trójkąta: "))
        pole = pole_trojkata(podstawa, wysokosc)
        print(f"Pole trójkąta wynosi: {pole} jednostek kwadratowych.")

    elif wybor == "3":
        promien = float(input("Podaj promień koła: "))
        pole = pole_kola(promien)
        print(f"Pole koła wynosi: {pole:.2f} jednostek kwadratowych.")

    else:
        print("Niepoprawny wybór.")

# Uruchomienie programuńŃ
wybierz_figure()