""" Zliczanie znaków:
Skrypt, który liczy, ile razy w tekście występują litery, cyfry i inne znaki. """   

def zlicz_znaki(tekst):
    """Funkcja licząca ilość liter, cyfr i innych znaków w tekście."""
    litery = cyfry = inne = 0

    for znak in tekst:
        if znak.isalpha():
            litery += 1
        elif znak.isdigit():
            cyfry += 1
        else:
            inne += 1

    return litery, cyfry, inne

# Pobranie tekstu od użytkownika
tekst = input("Podaj tekst: ")

# Obliczenie ilości znaków
litery, cyfry, inne = zlicz_znaki(tekst)

# Wyświetlenie wyników
print("\nStatystyki tekstu:")
print(f"Liczba liter: {litery}")
print(f"Liczba cyfr: {cyfry}")
print(f"Liczba innych znaków: {inne}")
ń