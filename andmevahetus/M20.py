loendur = 0

with open("arvud.txt", "r", encoding="utf-8") as sisendfail:
    with open("paarisarvud.txt", "w", encoding="utf-8") as valjundfail:
        for rida in sisendfail:
            rida = rida.strip()
            if rida:
                arv = int(rida)
                if arv % 2 == 0:
                    valjundfail.write(f"{arv}\n")
                    loendur += 1

print(f"Uude faili kirjutati {loendur} arvu.")