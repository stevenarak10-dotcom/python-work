kogutulu = 0
suurim_tulu = 0
parim_toode = ""
aruande_read = []

with open("muuk.txt", "r", encoding="utf-8") as fail:
    for rida in fail:
        osad = rida.strip().split()
        if not osad:
            continue
            
        toode = osad[0]
        hind = float(osad[1])
        kogus = int(osad[2])
        
        tulu = hind * kogus
        kogutulu += tulu

        if tulu > suurim_tulu:
            suurim_tulu = tulu
            parim_toode = toode
            
        aruande_read.append(f"{toode}: {tulu:.2f} €")

with open("muugiaruanne.txt", "w", encoding="utf-8") as valjundfail:
    valjundfail.write("MÜÜGIARUANNE\n")
    valjundfail.write("-" * 25 + "\n")
    for rida in aruande_read:
        valjundfail.write(rida + "\n")
    valjundfail.write("-" * 25 + "\n")
    valjundfail.write(f"Kogu müügitulu: {kogutulu:.2f} €\n")
    valjundfail.write(f"Suurima müügituluga toode: {parim_toode} ({suurim_tulu:.2f} €)\n")

print("Aruanne on edukalt salvestatud faili muugiaruanne.txt!")
