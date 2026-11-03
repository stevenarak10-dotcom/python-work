import string
koige_pikem_sona = ""
suurim_pikkus = 0
with open("tekst.txt", "r", encoding="utf-8") as fail:
    for rida in fail:
        sõnad = rida.split()
        
        for sõna in sõnad:
            puhas_sona = sõna.strip(string.punctuation)

            if len(puhas_sona) > suurim_pikkus:
                suurim_pikkus = len(puhas_sona)
                koige_pikem_sona = puhas_sona

if suurim_pikkus > 0:
    print(f"Kõige pikem sõna on: {koige_pikem_sona}")
    print(f"Selle pikkus on: {suurim_pikkus} tähte")
else:
    print("Failis ei olnud ühtegi sõna.")