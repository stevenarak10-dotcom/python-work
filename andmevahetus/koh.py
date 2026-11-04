import os

naidisandmed = """Mari 80 90 85
Jüri 60 70 55
Anna 95 89 90
Peeter 40 50 50
Kati 85 80 80
Martin 65 74 70
Laura 92 98 90
Rasmus 50 50 50"""

if not os.path.exists("tulemused.txt"):
    with open("tulemused.txt", "w", encoding="utf-8") as f:
        f.write(naidisandmed.strip())

if not os.path.exists("tulemused.txt"):
    print("Viga: Lähtefaili 'tulemused.txt' ei leitud! Palun veendu, et fail asub samas kaustas.")
else:
    opilaste_andmed = []
    koik_keskmised = []
    positiivsed_loendur = 0

    with open("tulemused.txt", "r", encoding="utf-8") as fail:
        for rida in fail:
            rida = rida.strip()
            if not rida:
                continue

            osad = rida.split()
            nimi = osad[0]
            tulemused = [float(x) for x in osad[1:]]
            keskmine = sum(tulemused) / len(tulemused) if len(tulemused) > 0 else 0
            koik_keskmised.append(keskmine)

            if 90 <= keskmine <= 100:
                hinne = 5
            elif 75 <= keskmine < 90:
                hinne = 4
            elif 60 <= keskmine < 75:
                hinne = 3
            elif 50 <= keskmine < 60:
                hinne = 2
            else:
                hinne = 1

            if hinne >= 3:
                positiivsed_loendur += 1
                
            opilaste_andmed.append({
                "nimi": nimi,
                "keskmine": keskmine,
                "hinne": hinne
            })

    klassi_keskmine = sum(koik_keskmised) / len(koik_keskmised) if len(koik_keskmised) > 0 else 0
    parim_opilane = max(opilaste_andmed, key=lambda x: x["keskmine"])["nimi"]
    norgim_opilane = min(opilaste_andmed, key=lambda x: x["keskmine"])["nimi"]

    valjund = []
    valjund.append("ÕPILASTE TULEMUSTE ARUANNE")
    valjund.append("-" * 30)
    valjund.append("")

    for opilane in opilaste_andmed:
        valjund.append(f"{opilane['nimi']:<12}Keskmine: {opilane['keskmine']:<7.2f}Hinne: {opilane['hinne']}")

    valjund.append("")
    valjund.append("-" * 30)
    valjund.append(f"Klassi keskmine: {klassi_keskmine:.2f}")
    valjund.append(f"Parim õpilane: {parim_opilane}")
    valjund.append(f"Nõrgim õpilane: {norgim_opilane}")
    valjund.append(f"Positiivse hindega õpilasi: {positiivsed_loendur}")

    kogu_tekst = "\n".join(valjund)

    print(kogu_tekst)
    with open("aruanne.txt", "w", encoding="utf-8") as fail_valjund:
        fail_valjund.write(kogu_tekst)
        
    print("\n[Info] Fail 'aruanne.txt' on edukalt loodud ja sisaldab sama kokkuvõtet.")
    osad = rida.split()

if len(osad) > 1:
    nimi = osad[0]
    tulemused = [float(x) for x in osad[1:]]
    keskmine = sum(tulemused) / len(tulemused) if len(tulemused) > 0 else 0
else:
    print(f"Viga: Real '{rida}' puuduvad tulemused. Palun veendu, et iga õpilase järel oleks vähemalt üks tulemus.")