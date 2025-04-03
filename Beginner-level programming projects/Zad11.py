""" Sortowanie liczb:
Program, który sortuje listę liczb podaną przez użytkownika w porządku rosnącym lub malejącym. """

def sortuj_liczby(liczby, kierunek):
    """Sortuje listę liczb w podanym kierunku."""
    if kierunek == "rosnąco":
        return sorted(liczby)
    elif kierunek == "malejąco":
        return sorted(liczby, reverse=True)
    else:
        print("Niepoprawny wybór sortowania.")
        return None

# Pobranie liczb od użytkownika
wejscie = input("Podaj liczby oddzielone przecinkami: ")
liczby = [int(x.strip()) for x in wejscie.split(",")]

# Wybór kierunku sortowania
kierunek = input("Wybierz sposób sortowania (rosnąco/malejąco): ").lower()

# Sortowanie i wyświetlenie wyniku
posortowane = sortuj_liczby(liczby, kierunek)

if posortowane:
    print(f"\nPosortowane liczby ({kierunek}): {posortowane}")
