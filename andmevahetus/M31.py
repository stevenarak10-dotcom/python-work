kontaktid = {}

with open("kontaktid.txt", "r", encoding="utf-8") as fail:
    for rida in fail:
        rida = rida.strip()
        if rida:
            nimi, epost, telefon = rida.split(";")
            kontaktid[nimi.lower()] = (nimi, epost, telefon)

while True:
    otsitav = input("\nSisesta otsitav nimi (lõpetamiseks vajuta Enter): ").strip()
    
    if otsitav == "":
        print("Programm lõpetatud.")
        break
    
    voti = otsitav.lower()
    if voti in kontaktid:
        nimi, epost, telefon = kontaktid[voti]
        print(f"Kontakt: {nimi}")
        print(f"E-post: {epost}")
        print(f"Telefon: {telefon}")
    else:
        print("Sellise nimega kontakti ei leitud.")