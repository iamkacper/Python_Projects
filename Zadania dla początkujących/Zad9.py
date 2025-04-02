""" Operacje na plikach:
Program, który tworzy nowy plik tekstowy, zapisuje do niego dane i umożliwia odczytanie jego zawartości. """

import os

def zapisz_do_pliku(nazwa_pliku, dane):
    """Funkcja zapisująca dane do pliku."""
    with open(nazwa_pliku, "w", encoding="utf-8") as plik:
        plik.write(dane)
    print(f"Dane zapisane do pliku: {nazwa_pliku}")

def odczytaj_plik(nazwa_pliku):
    """Funkcja odczytująca zawartość pliku."""
    try:
        with open(nazwa_pliku, "r", encoding="utf-8") as plik:
            zawartosc = plik.read()
        print(f"\nZawartość pliku {nazwa_pliku}:")
        print(zawartosc)
    except FileNotFoundError:
        print("Plik nie istnieje. Najpierw zapisz dane.")

def usun_plik(nazwa_pliku):
    """Funkcja usuwająca plik."""
    try:
        os.remove(nazwa_pliku)
        print(f"Plik {nazwa_pliku} został usunięty.")
    except FileNotFoundError:
        print("Plik nie istnieje, nie można go usunąć.")

# Pobranie danych od użytkownika
nazwa_pliku = input("Podaj nazwę pliku: ") + ".txt"

while True:
    print("\nWybierz operację:")
    print("1. Zapisz dane do pliku")
    print("2. Odczytaj plik")
    print("3. Usuń plik")
    print("4. Wyjdź")
    
    wybor = input("Twój wybór: ")

    if wybor == "1":
        dane = input("Wpisz tekst do zapisania w pliku: ")
        zapisz_do_pliku(nazwa_pliku, dane)
    elif wybor == "2":
        odczytaj_plik(nazwa_pliku)
    elif wybor == "3":
        usun_plik(nazwa_pliku)
    elif wybor == "4":
        print("Zamykanie programu...")
        break
    else:
        print("Niepoprawny wybór, spróbuj ponownie.")
