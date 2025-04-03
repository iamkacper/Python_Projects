"""     3.	Sprawdzanie siły hasła:
Skrypt sprawdzający, czy hasło jest wystarczająco silne, analizując jego długość i obecność różnych znaków (litery, cyfry, znaki specjalne)."""

import re  # Moduł do obsługi wyrażeń regularnych

def sprawdz_sile_hasla(haslo):
    """Funkcja sprawdzająca siłę hasła na podstawie długości i znaków specjalnych."""
    
    # Kryteria oceny hasła
    dlugosc = len(haslo) >= 8
    male_litery = bool(re.search(r"[a-z]", haslo))
    duze_litery = bool(re.search(r"[A-Z]", haslo))
    cyfry = bool(re.search(r"[0-9]", haslo))
    znaki_specjalne = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", haslo))

    # Ocena siły hasła
    sila = sum([dlugosc, male_litery, duze_litery, cyfry, znaki_specjalne])

    # Komunikat o sile hasła
    if sila == 5:
        return "🟢 Bardzo silne hasło!"
    elif sila == 4:
        return "🟡 Silne hasło."
    elif sila == 3:
        return "🟠 Średnie hasło – warto dodać znaki specjalne lub cyfry."
    else:
        return "🔴 Słabe hasło – użyj co najmniej 8 znaków, liter, cyfr i znaków specjalnych!"

# Pętla do wielokrotnego sprawdzania haseł
while True:
    haslo = input("🔑 Podaj hasło do sprawdzenia (lub wpisz 'exit' aby zakończyć): ")
    
    if haslo.lower() == "exit":
        print("👋 Zakończono program.")
        break  # Wyjście z pętli
    
    wynik = sprawdz_sile_hasla(haslo)
    print("\n📌 Wynik analizy:", wynik, "\n")

