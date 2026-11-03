arvud = []

with open('arvud.txt', 'r', encoding='utf-8') as fail:
    for rida in fail:
        arv = int(rida.strip())
        print(arv)
        
        arvud.append(arv)

summa = sum(arvud)
print()
print(f"Arvud: {arvud}")
print(f"Summa: {summa}")
