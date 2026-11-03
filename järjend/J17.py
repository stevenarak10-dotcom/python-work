algus = int(input("Algus: "))
lopp = int(input("Lõpp: "))

summa = 0

for arv in range(algus, lopp + 1):
    summa += arv

print(f"Summa: {summa}")