""" 4.	Szyfrator Cezara:
Program implementujący szyfr Cezara, który przesuwa litery w alfabecie o określoną liczbę pozycji, 
umożliwiając szyfrowanie i deszyfrowanie wiadomości."""

def szyfr_cezara(tekst, klucz, tryb="szyfruj"):
    """Funkcja szyfrująca i deszyfrująca tekst za pomocą Szyfru Cezara."""
    wynik = ""
    
    # Jeśli użytkownik chce odszyfrować, odwracamy klucz (przesuwamy w lewo)
    if tryb == "deszyfruj":
        klucz = -klucz
    
    for znak in tekst:
        if znak.isalpha():  # Sprawdzamy, czy znak to litera
            kod_podstawowy = ord('A') if znak.isupper() else ord('a')
            nowy_znak = chr((ord(znak) - kod_podstawowy + klucz) % 26 + kod_podstawowy)
            wynik += nowy_znak
        else:
            wynik += znak  # Znaki specjalne i cyfry zostają bez zmian
    
    return wynik

# Pętla do wielokrotnego użycia
while True:
    print("\n🔹 SZYFR CEZARA 🔹")
    wybor = input("Wybierz opcję: (1) Szyfrowanie, (2) Deszyfrowanie, (3) Wyjście: ")

    # Sprawdzamy, czy wybór jest większy niż 4
    if wybor.isdigit() and int(wybor) > 4:
        print("❌ Błędny wybór! Program zakończony.")
        break  # Zakończenie programu w przypadku błędnego wyboru większego niż 4
    
    # Sprawdzamy, czy wybór jest prawidłowy (1, 2, 3)
    if wybor not in ["1", "2", "3"]:
        print("❌ Błędny wybór! Proszę wybrać opcję 1, 2 lub 3.")
        continue  # Pozwala na ponowne podanie opcji bez kończenia programu

    if wybor == "3":
        print("👋 Zakończono program.")
        break  # Wyjście z programu
    
    tekst = input("✍️ Wpisz tekst: ")
    klucz = int(input("🔑 Podaj klucz przesunięcia (np. 3): "))

    if wybor == "1":
        print("\n🔒 Zaszyfrowany tekst:", szyfr_cezara(tekst, klucz, "szyfruj"))
    elif wybor == "2":
        print("\n🔓 Odszyfrowany tekst:", szyfr_cezara(tekst, klucz, "deszyfruj"))

