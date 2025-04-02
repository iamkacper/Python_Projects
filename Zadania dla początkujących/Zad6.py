""" Tabliczka mnożenia:
Skrypt generujący tabliczkę mnożenia dla liczby podanej przez użytkownika, umożliwiający naukę matematyki. """

def tabliczka_mnozenia(liczba, x, y):
    """Funkcja generująca tabliczkę mnożenia dla podanej liczby w określonym zakresie."""
    print(f"\nTabliczka mnożenia dla liczby {liczba} od {x} do {y}:")
    for i in range(x, y + 1):  # Zakres od x do y
        wynik = liczba * i
        print(f"{liczba} x {i} = {wynik}")

# Pętla do wielokrotnego generowania tabliczki mnożenia
while True:
    try:
        liczba = int(input("Podaj liczbę, dla której chcesz zobaczyć tabliczkę mnożenia: "))
        x = int(input("Podaj początkową liczbę zakresu (np. 1): "))
        y = int(input("Podaj końcową liczbę zakresu (np. 10): "))
        
        # Sprawdzamy, czy zakres jest poprawny
        if x > y:
            print("❌ Początkowa liczba zakresu musi być mniejsza lub równa końcowej liczbie.")
            continue
        ń
        # Generowanie tabliczki mnożenia
        tabliczka_mnozenia(liczba, x, y)

    except ValueError:
        print("❌ Proszę podać prawidłową liczbę!")

    # Zapytanie, czy użytkownik chce wygenerować tabliczkę dla innej liczby
    kontynuacja = input("\nCzy chcesz wygenerować tabliczkę dla innej liczby? (tak/nie): ").lower()
    if kontynuacja != "tak":
        print("👋 Zakończono program.")
        break