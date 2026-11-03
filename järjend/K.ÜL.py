opilased = {
    "kati": {"nimi": "Kati", "punktid": 94, "hinne": 5},
    "mati": {"nimi": "Mati", "punktid": 75, "hinne": 4},
    "juku": {"nimi": "Juku", "punktid": 52, "hinne": 3}
}

sisestus = input("Sisesta õpilase nimi: ")

otsitav_nimi = sisestus.lower()

if otsitav_nimi in opilased:
    andmed = opilased[otsitav_nimi]
    print(f"\nÕpilane: {andmed['nimi']}")
    print(f"Punktid: {andmed['punktid']}")
    print(f"Hinne: {andmed['hinne']}")
else:
    print("\nSellist õpilast ei leitud.")
