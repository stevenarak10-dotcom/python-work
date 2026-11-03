esimene = [12, 15, 18]
teine = [21, 24, 27]

uus_järjend = esimene + teine

uus_järjend.append(30)

print("Uus järjend:", uus_järjend)

print("Esimene element:", uus_järjend[0])
print("Viimane element:", uus_järjend[-1])

koikide_summa = sum(uus_järjend)
print("Kõigi arvude summa:", koikide_summa)