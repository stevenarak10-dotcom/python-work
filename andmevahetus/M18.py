arvud_sisend = []
for i in range(5):
    arv = int(input(f"Sisesta {i+1}. täisarv: "))
    arvud_sisend.append(arv)

with open("sisestatud_arvud.txt", "w", encoding="utf-8") as fail:
    for arv in arvud_sisend:
        fail.write(str(arv) + "\n")

loetud_arvud = []
with open("sisestatud_arvud.txt", "r", encoding="utf-8") as fail:
    for rida in fail:
        if rida.strip():
            loetud_arvud.append(int(rida.strip()))


summa = sum(loetud_arvud)
keskmine = summa / len(loetud_arvud)
arvud_tekstina = ", ".join(map(str, loetud_arvud))

print()
print(f"Sisestatud arvud: {arvud_tekstina}")
print(f"Summa: {summa}")
print(f"Keskmine: {keskmine}")