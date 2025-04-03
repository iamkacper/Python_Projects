""" Obliczanie liczby pierwszych:
Skrypt, który sprawdza, czy liczba wprowadzona przez użytkownika jest liczbą pierwszą. """

def czy_liczba_pierwsza(liczba):
    """Funkcja sprawdza, czy liczba jest pierwsza."""
    if liczba < 2:
        return False
    for i in range(2, int(liczba ** 0.5) + 1):
        if liczba % i == 0:
            return False
    return True

# Pobranie liczby od użytkownika
liczba = int(input("Podaj liczbę: "))

# Sprawdzenie i wyświetlenie wyniku
if czy_liczba_pierwsza(liczba):
    print(f"{liczba} jest liczbą pierwszą.")
else:
    print(f"{liczba} nie jest liczbą pierwszą.")
