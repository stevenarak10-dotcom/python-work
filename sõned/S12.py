lause = input("Sisesta lause: ")
otsitav = input("Sisesta otsitav: ")

indeks = lause.find(otsitav)

if indeks != -1:
    print(f"Leitud indeksilt {indeks}.")
else:
    print("Otsitavat tekstiosa lausest ei leitud.")
