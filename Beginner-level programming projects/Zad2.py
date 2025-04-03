""" 2.Podstawowe obliczenia: Program, który przyjmuje dwie liczby od użytkownika i 
wykonuje na nich podstawowe operacje matematyczne: dodawanie, odejmowanie, mnożenie i dzielenie. """

# Pobranie liczb od użytkownika
num1 = float(input("Podaj pierwszą liczbę: "))
num2 = float(input("Podaj drugą liczbę: "))

# Wykonanie podstawowych operacji matematycznych
suma = num1 + num2
roznica = num1 - num2
iloczyn = num1 * num2
if num2 != 0:
    iloraz = num1 / num2
else:
    iloraz = "Nie można dzielić przez zero!"

# Wyświetlenie wyników
print("\n📌 Wyniki obliczeń:")
print(f"Dodawanie: {num1} + {num2} = {suma}")
print(f"Odejmowanie: {num1} - {num2} = {roznica}")
print(f"Mnożenie: {num1} * {num2} = {iloczyn}")
print(f"Dzielenie: {num1} / {num2} = {iloraz}")