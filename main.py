# --- FUNKCJE ---




# --- GLOWNY PROGRAM ---

# Pobieranie danych od uzytkownika
n = int(input("Podaj liczbe punktow (n): "))
wszystkie_punkty = []

print(f"Podaj wspolrzedne {n} punktow w formacie: x y")
for i in range(n):
    wejscie = input(f"Punkt {i+1}: ").split()
    x, y = float(wejscie[0]), float(wejscie[1])
    wszystkie_punkty.append((x, y))

# Obliczenia
#wynik_jarvis = algorytm_jarvisa(wszystkie_punkty)
#wynik_graham = algorytm_grahama(wszystkie_punkty)

# Porownanie i wyswietlenie wynikow
print("\n--- POROWNANIE WYNIKOW ---")
print(f"Otoczka Jarvisa ({len(wynik_jarvis)} wierzcholkow):", wynik_jarvis)
print(f"Otoczka Grahama ({len(wynik_graham)} wierzcholkow):", wynik_graham)

if set(wynik_jarvis) == set(wynik_graham):
    print("\nWyniki sa identyczne.")
else:
    print("\nWyniki sie roznia.")