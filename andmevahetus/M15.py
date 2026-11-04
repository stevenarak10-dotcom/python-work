nimi = input("Sisesta nimi: ")
vanus = input("Sisesta vanus: ")
epost = input("Sisesta e-posti aadress: ")

with open("kasutaja.txt", "w", encoding="utf-8") as fail:
    fail.write(nimi + "\n")
    fail.write(vanus + "\n")
    fail.write(epost + "\n")

print("\n--- Andmed salvestatud! ---\n")

print("Faili sisu terminalis:")
with open("kasutaja.txt", "r", encoding="utf-8") as fail:
    sisu = fail.read()
    print(sisu)