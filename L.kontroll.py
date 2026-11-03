
nimi = input("Nimi:Steven ")
vanus = int(input("Vanus:16 "))
koolitee_km = int(input("Koolitee pikkus kilomeetrites:12 "))
koolitee_min = int(input("Koolitee kestus minutites:30 "))


vanus_järgmisel_aastal = vanus + 1
koolitee_meetrites = int(koolitee_km * 1000)
tunnid = koolitee_min // 60
minutid = koolitee_min % 60


keskmine_kiirus = koolitee_km / (koolitee_min / 60)

print(f"Tere, {nimi}!")
print(f"Järgmisel aastal oled {vanus_järgmisel_aastal}-aastane.")
print(f"Sinu koolitee pikkus on {koolitee_meetrites} meetrit.")
print(f"Koolitee kestab {tunnid} tundi ja {minutid} minutit.")
print(f"Keskmine kiirus on {keskmine_kiirus} km/h.")