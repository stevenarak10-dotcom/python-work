hinded = []
opilased_vabalt_4 = []
with open("hinded.txt", "r", encoding="utf-8") as fail:
    for rida in fail:
        rida = rida.strip()
        if rida:
            osad = rida.split()
            nimi = osad[0]
            hinne = int(osad[1])
            hinded.append(hinne)

            if hinne >= 4:
                opilased_vabalt_4.append(nimi)

keskmine = sum(hinded) / len(hinded)
korgeim = max(hinded)
madalaim = min(hinded)

print(f"Keskmine hinne: {keskmine:.2f}")
print(f"Kõrgeim hinne: {korgeim}")
print(f"Madalaim hinne: {madalaim}")
print()
print("Õpilased hindega vähemalt 4:")
for nimi in opilased_vabalt_4:
    print(nimi)