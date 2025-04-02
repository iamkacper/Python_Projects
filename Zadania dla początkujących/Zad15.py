""" Sortowanie słów:
Skrypt, który sortuje słowa w ciągu tekstowym w porządku alfabetycznym. """

def sortuj_slowa(tekst):
    """Funkcja sortująca słowa w tekście w porządku alfabetycznym."""
    # Dzielimy tekst na słowa
    slowa = tekst.split()

    # Sortujemy słowa alfabetycznie
    slowa.sort()

    # Łączymy posortowane słowa w jeden ciąg tekstowy
    posortowany_tekst = " ".join(slowa)

    return posortowany_tekst

# Pobranie tekstu od użytkownika
tekst = input("Podaj tekst do posortowania: ")

# Sortowanie słów w tekście
posortowany_tekst = sortuj_slowa(tekst)

# Wyświetlenie posortowanego tekstu
print("Posortowany tekst:", posortowany_tekst)