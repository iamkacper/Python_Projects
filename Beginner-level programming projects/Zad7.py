""" Konwerter jednostek:
Program do konwertowania jednostek (np. z kilometrów na metry, stopni Celsjusza na Fahrenheita) na podstawie danych wejściowych. """

def konwertuj_jednostki():
    """Funkcja konwertująca jednostki na podstawie wyboru użytkownika."""
    print("\nWybierz jednostkę do konwersji:")
    print("1. Kilometry na metry")
    print("2. Metry na kilometry")
    print("3. Celsjusz na Fahrenheit")
    print("4. Fahrenheit na Celsjusz")
    print("5. Gramy na kilogramy")
    print("6. Kilogramy na gramy")
    
    wybor = input("Podaj numer wyboru (1-6): ")

    try:
        if wybor == "1":
            km = float(input("Podaj liczbę kilometrów: "))
            print(f"{km} km = {km * 1000} metrów")
        
        elif wybor == "2":
            m = float(input("Podaj liczbę metrów: "))
            print(f"{m} metrów = {m / 1000} km")
        
        elif wybor == "3":
            celsiusz = float(input("Podaj temperaturę w Celsjuszach: "))
            fahrenheit = (celsiusz * 9/5) + 32
            print(f"{celsiusz}°C = {fahrenheit}°F")
        
        elif wybor == "4":
            fahrenheit = float(input("Podaj temperaturę w Fahrenheitach: "))
            celsiusz = (fahrenheit - 32) * 5/9
            print(f"{fahrenheit}°F = {celsiusz}°C")
        
        elif wybor == "5":
            gram = float(input("Podaj liczbę gramów: "))
            print(f"{gram} g = {gram / 1000} kg")
        
        elif wybor == "6":
            kilogram = float(input("Podaj liczbę kilogramów: "))
            print(f"{kilogram} kg = {kilogram * 1000} g")
        
        else:
            print("❌ Niepoprawny wybór!")

    except ValueError:
        print("❌ Proszę podać prawidłową liczbę!")

# Pętla do wielokrotnego korzystania z konwertera
while True:
    konwertuj_jednostki()

    # Zapytanie, czy użytkownik chce kontynuować
    kontynuacja = input("\nCzy chcesz przeprowadzić kolejną konwersję? (tak/nie): ").lower()
    if kontynuacja != "tak":
        print("👋 Zakończono program.")
        break
