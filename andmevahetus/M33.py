import os
def loe_nimed(failinimi):
    with open(failinimi, "r", encoding="utf-8") as fail:
        return {rida.strip() for rida in fail if rida.strip()}

nimed1 = loe_nimed("nimekiri1.txt")
nimed2 = loe_nimed("nimekiri2.txt")

molemas = sorted(nimed1 & nimed2)
ainult_esimeses = sorted(nimed1 - nimed2)
ainult_teises = sorted(nimed2 - nimed1)

with open("vordlus.txt", "w", encoding="utf-8") as valjundfail:
    valjundfail.write("Mõlemas failis esinevad nimed:\n")
    for nimi in molemas:
        valjundfail.write(f"- {nimi}\n")
        
    valjundfail.write("\nAinult esimeses failis olevad nimed:\n")
    for nimi in ainult_esimeses:
        valjundfail.write(f"- {nimi}\n")
        
    valjundfail.write("\nAinult teises failis olevad nimed:\n")
    for nimi in ainult_teises:
        valjundfail.write(f"- {nimi}\n")

print("Võrdluse tulemused on salvestatud faili vordlus.txt.")