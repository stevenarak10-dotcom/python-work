sõnad = ["Python", "programmeerimine", "järjend", "tsükkel", "fail"]

for sõna in sõnad:
    pikkus = len(sõna)
    print(f"{sõna} - {pikkus} tähemärki")
    print(f"Esimese ja viimase tähe täiendus: {sõna[0]} ja {sõna[-1]}")