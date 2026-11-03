kogus = int(input("Mitu arvu soovid sisestada? "))

summa = 0

for i in range(kogus):
    arv = int(input("Sisesta arv: "))
    summa += arv

keskmine = summa / kogus

print()
print(f"Summa: {summa}")
print(f"Keskmine: {keskmine}")
