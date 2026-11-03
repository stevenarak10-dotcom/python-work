arvud = [-12, 5, 0, 18, -7, 23, -3, 9]

positiivsed_arv = 0
negatiivsed_arv = 0
nullid_arv = 0
positiivsed_summa = 0
negatiivsed_jarjend = []

for arv in arvud:
    if arv > 0:
        positiivsed_arv += 1
        positiivsed_summa += arv
    elif arv < 0:
        negatiivsed_arv += 1
        negatiivsed_jarjend.append(arv)
    else:
        nullid_arv += 1

print(f"1. Positiivsete arvude arv: {positiivsed_arv}")
print(f"2. Negatiivsete arvude arv: {negatiivsed_arv}")
print(f"3. Nullide arv: {nullid_arv}")
print(f"4. Positiivsete arvude summa: {positiivsed_summa}")
print(f"5. Uus järjend negatiivsetest arvudest: {negatiivsed_jarjend}")