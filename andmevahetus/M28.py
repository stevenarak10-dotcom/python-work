andmed = []

with open("temperatuurid.txt", "r", encoding="utf-8") as fail:
    for rida in fail:
        rida = rida.strip()
        if rida:
            osad = rida.split()
            päev = osad[0]
            temp = float(osad[1])
            andmed.append((päev, temp))

temperatuurid = [temp for päev, temp in andmed]
keskmine = sum(temperatuurid) / len(temperatuurid)

soojem_päev, max_temp = max(andmed, key=lambda x: x[1])
külmem_päev, min_temp = min(andmed, key=lambda x: x[1])

üle_15 = sum(1 for päev, temp in andmed if temp > 15)

with open("temperatuuri_aruanne.txt", "w", encoding="utf-8") as valjundfail:
    valjundfail.write(f"Nädala keskmine temperatuur: {keskmine:.2f} kraadi\n")
    valjundfail.write(f"Kige soojem päev: {soojem_päev} ({max_temp:g} kraadi)\n")
    valjundfail.write(f"Kõige külmem päev: {külmem_päev} ({min_temp:g} kraadi)\n")
    valjundfail.write(f"Päevi üle 15 kraadi: {üle_15}\n")

print("Aruanne on edukalt salvestatud faili temperatuuri_aruanne.txt.")