from operator import itemgetter

slownik_aktywnosci = {}
slownik_akt_id = {}
suma_czasu_akt = []
ilosc_akt = 0

while(1 > 0):
    x = input("Dodaj Aktywnosc (dodaj) lub Pokaz Czas (suma) lub Pokaz Top (top): ")
    if(x == "dodaj"):
        x = input("Nazwa aktywnosci: ")
        y = int(input("Czas aktywnosci: "))
        if (x not in slownik_aktywnosci):
            slownik_aktywnosci[x] = []
            slownik_aktywnosci[x].append(y)
        else:
            slownik_aktywnosci[x].append(y)
        if(len(slownik_aktywnosci[x]) == 1):
            slownik_akt_id[x] = ilosc_akt
            ilosc_akt += 1
        suma_czasu_akt.append([0, 0])
        suma_czasu_akt[slownik_akt_id[x]] = [int(sum(slownik_aktywnosci[x])), x]

    if (x == "suma"):
        x = input("Podaj nazwe aktywnosci: ")
        print(sum(slownik_aktywnosci[x]))
    if (x == "top"):
        suma_czasu_akt = sorted(suma_czasu_akt, key=itemgetter(0))
        print(suma_czasu_akt[-1])
        print(suma_czasu_akt[-2])
        print(suma_czasu_akt[-3])

