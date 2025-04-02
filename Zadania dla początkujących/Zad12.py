""" Znajdowanie średniej:
Skrypt, który oblicza średnią arytmetyczną liczb wprowadzonych przez użytkownika. """

def oblicz_srednia(liczby):
    """Funkcja obliczająca średnią arytmetyczną."""
    if len(liczby) == 0:
        return 0
    return sum(liczby) / len(liczby)

# Pobranie liczb od użytkownika
wejscie = input("Podaj liczby oddzielone przecinkami: ")
liczby = [float(x.strip()) for x in wejscie.split(",")]

# Obliczanie średniej
srednia = oblicz_srednia(liczby)

# Wyświetlenie wyniku
print(f"\nŚrednia arytmetyczna liczb: {srednia}")