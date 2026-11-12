import os

ANDMEFAIL = "kulud.txt"
KOKKUVOTTEFAIL = "kokkuvote.txt"

def loe_kulud():
    kulud = []
    if not os.path.exists(ANDMEFAIL):
        return kulud
    
    with open(ANDMEFAIL, "r", encoding="utf-8") as fail:
        for rida in fail:
            rida = rida.strip()
            if rida:
                osad = rida.split(";")
                if len(osad) == 4:
                    kulud.append({
                        "kuupaev": osad[0],
                        "kategooria": osad[1],
                        "kirjeldus": osad[2],
                        "summa": float(osad[3])
                    })
    return kulud

def lisa_kulu():
    print("\n--- Uue kulu lisamine ---")
    kuupaev = input("Sisesta kuupäev (nt 15.10.2026): ").strip()
    kategooria = input("Sisesta kategooria (nt Toit, Transport): ").strip()
    kirjeldus = input("Sisesta kirjeldus: ").strip()
    
    try:
        summa = float(input("Sisesta summa (\u20ac): ").replace(",", "."))
    except ValueError:
        print("Viga! Summa peab olema number.")
        return

    with open(ANDMEFAIL, "a", encoding="utf-8") as fail:
        fail.write(f"{kuupaev};{kategooria};{kirjeldus};{summa:.2f}\n")
    print("Kulu on edukalt salvestatud!")

def kuva_koik_kulud():
    kulud = loe_kulud()
    print("\n--- Kõik kulud ---")
    if not kulud:
        print("Kulusid ei leitud.")
        return
    
    for k in kulud:
        print(f"{k['kuupaev']} | {k['kategooria']} | {k['kirjeldus']} | {k['summa']:.2f} €")

def arvuta_kogukulu():
    kulud = loe_kulud()
    kogusumma = sum(k["summa"] for k in kulud)
    print(f"\nKogukulu kokku: {kogusumma:.2f} €")

def kuva_kategooria_kulud():
    kulud = loe_kulud()
    otsitav = input("\nSisesta kategooria nimi: ").strip().lower()
    leitud = [k for k in kulud if k["kategooria"].lower() == otsitav]
    
    print(f"\n--- Kategooria '{otsitav.capitalize()}' kulud ---")
    if not leitud:
        print("Selles kategoorias kulusid ei leitud.")
        return
    
    kategooria_summa = 0
    for k in leitud:
        print(f"{k['kuupaev']} | {k['kirjeldus']} | {k['summa']:.2f} €")
        kategooria_summa += k["summa"]
    print(f"Kategooria kogukulu: {kategooria_summa:.2f} €")

def salvesta_kokkuvote():
    kulud = loe_kulud()
    if not kulud:
        print("\nAndmed puuduvad, kokkuvõtet ei loodud.")
        return

    kogusumma = sum(k["summa"] for k in kulud)
    kategooriad = {}
    for k in kulud:
        kat = k["kategooria"]
        kategooriad[kat] = kategooriad.get(kat, 0) + k["summa"]

    with open(KOKKUVOTTEFAIL, "w", encoding="utf-8") as fail:
        fail.write("KULUDE KOKKUVÕTE\n")
        fail.write("=" * 30 + "\n")
        fail.write(f"Kirjete arv: {len(kulud)}\n")
        fail.write(f"Kogukulu: {kogusumma:.2f} €\n\n")
        fail.write("Kulud kategooriate kaupa:\n")
        for kat, summa in kategooriad.items():
            fail.write(f"- {kat}: {summa:.2f} €\n")
            
    print(f"\nKokkuvõte on salvestatud faili {KOKKUVOTTEFAIL}!")
    
while True:
    print("\n=== KULUDE ARVESTAMISE PROGRAMM ===")
    print("1. Lisa uus kulu")
    print("2. Kuva kõik kulud")
    print("3. Arvuta kogukulu")
    print("4. Kuva valitud kategooria kulud")
    print("5. Salvesta kokkuvõte faili")
    print("0. Välju")
    
    valik = input("Vali tegevus (0-5): ").strip()
    
    if valik == "1":
        lisa_kulu()
    elif valik == "2":
        kuva_koik_kulud()
    elif valik == "3":
        arvuta_kogukulu()
    elif valik == "4":
        kuva_kategooria_kulud()
    elif valik == "5":
        salvesta_kokkuvote()
    elif valik == "0":
        print("Programm suletud.")
        break
    else:
        print("Tundmatu valik, proovi uuesti.")