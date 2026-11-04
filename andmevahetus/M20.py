näidis_arvud = [12, 7, 8, 15, 4, 32, 9]
with open("arvud.txt", "w", encoding="utf-8") as fail:
    for arv in näidis_arvud:
        fail.write(str(arv) + "\n")
kirjutatud_arvude_arv = 0

with open("arvud.txt", "r", encoding="utf-8") as algfail, \
     open("paarisarvud.txt", "w", encoding="utf-8") as uus_fail:
     
    for rida in algfail:
        if rida.strip():
            arv = int(rida.strip())

            if arv % 2 == 0:
                uus_fail.write(str(arv) + "\n")
                kirjutatud_arvude_arv += 1

print(f"Uude faili kirjutati {kirjutatud_arvude_arv} arvu.")