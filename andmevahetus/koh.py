import os

SISENDFAIL = "tulemused.txt"
VALJUNDFAIL = "aruanne.txt"

def määra_hinne(keskmine):
    """Määrab hinde vastavalt etteantud skaalale."""
    if keskmine >= 90:
        return 5
    elif keskmine >= 75:
        return 4
    elif keskmine >= 60:
        return 3
    elif keskmine >= 50:
        return 2
    else:
        return 1

def main():
    if not os.path.exists(SISENDFAIL):
        print(f"Viga: Lähtefaili '{SISENDFAIL}' ei leitud!")
        return

    opilased = []

    with open(SISENDFAIL, "r", encoding="utf-8") as fail:
        for rea_nr, rida in enumerate(fail, start=1):
            rida = rida.strip()
            if not rida:
                continue

            osad = rida.split(";")
            if len(osad) != 4:
                print(f"Hoiatus: Rida {rea_nr} ('{rida}') on vigase vorminguga ja jäetakse vahele.")
                continue

            try:
                nimi = osad[0].strip()
                tulemused = [float(osad[1]), float(osad[2]), float(osad[3])]
            except ValueError:
                print(f"Hoiatus: Real {rea_nr} ('{rida}') ei ole punktid numbrid ja rida jäetakse vahele.")
                continue

            keskmine = sum(tulemused) / len(tulemused)
            hinne = määra_hinne(keskmine)

            opilased.append({
                "nimi": nimi,
                "keskmine": keskmine,
                "hinne": hinne
            })

    if not opilased:
        print("Viga: Failist ei leitud ühtegi korrektset õpilase rida.")
        print("Kontrolli, et failis 'tulemused.txt' oleksid andmed kujul: Mari;85;92;78")
        return

    klassi_keskmine = sum(o["keskmine"] for o in opilased) / len(opilased)
    parim_opilane = max(opilased, key=lambda o: o["keskmine"])["nimi"]
    norgim_opilane = min(opilased, key=lambda o: o["keskmine"])["nimi"]
    positiivseid = sum(1 for o in opilased if o["hinne"] >= 3)

    aruande_read = [
        "ÕPILASTE TULEMUSTE ARUANNE",
        "-" * 35
    ]

    for o in opilased:
        aruande_read.append(f"{o['nimi']:<10} Keskmine: {o['keskmine']:.2f}  Hinne: {o['hinne']}")

    aruande_read.append("-" * 35)
    aruande_read.append(f"Klassi keskmine: {klassi_keskmine:.2f}")
    aruande_read.append(f"Parim õpilane: {parim_opilane}")
    aruande_read.append(f"Nõrgim õpilane: {norgim_opilane}")
    aruande_read.append(f"Positiivse hindega õpilasi: {positiivseid}")

    lopptekst = "\n".join(aruande_read)

    print(lopptekst)

    with open(VALJUNDFAIL, "w", encoding="utf-8") as valjund:
        valjund.write(lopptekst + "\n")

if __name__ == "__main__":
    main()