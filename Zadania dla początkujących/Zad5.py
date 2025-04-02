""" Zadanie 5.	BMI Kalkulator
Program obliczający BMI (wskaźnik masy ciała) na podstawie wagi i wzrostu użytkownika, wskazując, czy wynik mieści się w normie. """

def oblicz_bmi(waga, wzrost):
    """Funkcja obliczająca BMI na podstawie wagi i wzrostu."""
    bmi = waga / (wzrost ** 2)
    return bmi

def kategoria_bmi(bmi):
    """Funkcja określająca kategorię BMI."""
    if bmi < 18.5:
        return "Niedowaga"
    elif 18.5 <= bmi < 24.9:
        return "Norma"
    elif 25 <= bmi < 29.9:
        return "Nadwaga"
    else:
        return "Otyłość"

# Pętla do wielokrotnego obliczania BMI
while True:
    print("\n🔹 KALKULATOR BMI 🔹")
    
    try:
        waga = float(input("Podaj wagę (w kg): "))
        wzrost = float(input("Podaj wzrost (w metrach): "))
        
        # Sprawdzamy, czy wartości są poprawne
        if waga <= 0 or wzrost <= 0:
            print("❌ Waga i wzrost muszą być liczbami dodatnimi! Spróbuj ponownie.")
            continue

        # Obliczanie BMI
        bmi = oblicz_bmi(waga, wzrost)
        kategoria = kategoria_bmi(bmi)

        # Wyświetlenie wyniku
        print(f"\n📊 Twoje BMI wynosi: {bmi:.2f}")
        print(f"🔍 Kategoria: {kategoria}")

    except ValueError:
        print("❌ Proszę podać prawidłowe liczby! Spróbuj ponownie.")
    
    # Zapytanie, czy użytkownik chce obliczyć kolejne BMI
    kontynuacja = input("\nCzy chcesz obliczyć kolejne BMI? (tak/nie): ").lower()
    if kontynuacja != "tak":
        print("👋 Zakończono program.")
        break
