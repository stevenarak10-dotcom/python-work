lause = input("Sisesta lause: ")
taht = input("Sisesta täht: ")

lause_madal = lause.lower()
taht_madal = taht.lower()

mitu_korda = 0

for sümbol in lause_madal:
    if sümbol == taht_madal:
        mitu_korda += 1

print(f"Täht {taht} esineb {mitu_korda} korda.")
