""" Prosty ping test:
Skrypt, który sprawdza dostępność serwera lub urządzenia w sieci za pomocą polecenia ping. """

import subprocess
import platform

def ping(host):
    """Funkcja sprawdzająca dostępność hosta w sieci za pomocą polecenia ping."""
    # Sprawdzamy system operacyjny, by dopasować polecenie ping
    system = platform.system().lower()

    # Wybieramy odpowiednią komendę dla systemu
    if system == "windows":
        command = ["ping", "-n", "4", host]  # 4 pingi w systemie Windows
    else:
        command = ["ping", "-c", "4", host]  # 4 pingi w systemach Unix (Linux/Mac)

    try:
        # Uruchamiamy polecenie ping i sprawdzamy, czy host odpowiada
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode == 0:
            print(f"Host {host} jest dostępny.")
        else:
            print(f"Host {host} jest niedostępny.")
    except Exception as e:
        print(f"Błąd podczas próby pingowania: {e}")

# Pobranie adresu hosta od użytkownika
host = input("Podaj adres IP lub nazwę hosta, który chcesz pingować: ")
ping(host)