with open('nimed.txt', 'r', encoding='utf-8') as fail:
    nimed = [rida.strip() for rida in fail.readlines()]
if nimed:
    print(f"Esimene nimi: {nimed[0]}")
    print(f"Viimane nimi: {nimed[-1]}")
else:
    print("Fail on tühi!")