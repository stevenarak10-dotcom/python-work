with open("tekst.txt", "r", encoding="utf-8") as fail:
    tekst = fail.read()

sonad = tekst.split()

sonade_arv = len(sonad)

print(f"Tekstis on {sonade_arv} sõna.")