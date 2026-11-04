max_hinnete_arv = -1
max_hinnetega_opilane = ""

with open("opilased.txt", "r", encoding="utf-8") as fail:
    for rida in fail:
        rida = rida.strip()
        if rida:
            osad = rida.split()
            nimi = osad[0]
            hinded = [int(h) for h in osad[1:]]

            hinnete_arv = len(hinded)
            keskmine_hinne = sum(hinded) / hinnete_arv

            print(f"Õpilane: {nimi}, Hinnete arv: {hinnete_arv}, Keskmine hinne: {keskmine_hinne:.2f}")
            if hinnete_arv > max_hinnete_arv:
                max_hinnete_arv = hinnete_arv
                max_hinnetega_opilane = nimi
print()
print(f"Kõige rohkem hindeid ({max_hinnete_arv} hinnet) on õpilasel: {max_hinnetega_opilane}")