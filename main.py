import math
import time


def iloczyn(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def odleglosc2(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2


def graham(punkty):
    punkty = list(set(punkty))

    if len(punkty) <= 1:
        return punkty

    start = min(punkty, key=lambda p: (p[1], p[0]))
    punkty.remove(start)

    punkty.sort(key=lambda p: (math.atan2(p[1] - start[1], p[0] - start[0]), odleglosc2(start, p)))

    otoczka = [start]

    for p in punkty:
        while len(otoczka) >= 2 and iloczyn(otoczka[-2], otoczka[-1], p) <= 0:
            otoczka.pop()
        otoczka.append(p)

    return otoczka


def jarvis(punkty):
    punkty = list(set(punkty))

    if len(punkty) <= 1:
        return punkty

    start = min(punkty, key=lambda p: (p[0], p[1]))
    otoczka = []
    punkt = start

    while True:
        otoczka.append(punkt)
        nastepny = punkty[0]

        for p in punkty:
            if p == punkt:
                continue

            if nastepny == punkt:
                nastepny = p
                continue

            skr = iloczyn(punkt, nastepny, p)

            if skr > 0:
                nastepny = p
            elif skr == 0 and odleglosc2(punkt, p) > odleglosc2(punkt, nastepny):
                nastepny = p

        punkt = nastepny

        if punkt == start:
            break

    return otoczka


def ta_sama_otoczka(o1, o2):
    return set(o1) == set(o2)


n = int(input("Podaj liczbę punktów: "))
punkty = []

print("Podaj punkty w formacie x y:")

for i in range(n):
    x, y = map(int, input().split())
    punkty.append((x, y))

start = time.perf_counter()
otoczka_graham = graham(punkty)
czas_graham = time.perf_counter() - start

start = time.perf_counter()
otoczka_jarvis = jarvis(punkty)
czas_jarvis = time.perf_counter() - start

print("\nOtoczka Grahama:")
for p in otoczka_graham:
    print(p)

print("\nOtoczka Jarvisa:")
for p in otoczka_jarvis:
    print(p)

print("\nPorównanie wyników:")
if ta_sama_otoczka(otoczka_graham, otoczka_jarvis):
    print("Oba algorytmy dały tę samą otoczkę.")
else:
    print("Wyniki są różne.")

print("\nCzasy działania:")
print("Graham:", round(czas_graham, 5), "s")
print("Jarvis:", round(czas_jarvis, 5), "s")

print("\nZłożoności:")
print("Graham: O(n log n)")
print("Jarvis: O(n * h), gdzie h to liczba punktów na otoczce")