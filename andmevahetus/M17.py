tooted = []

while True:
    toode = input("Sisesta toode: ")
    if toode == "STOP":
        break
    tooted.append(toode)

with open("ostunimekiri.txt", "a", encoding="utf-8") as fail:
    for toode in tooted:
        fail.write(toode + "\n")

print("\nOstunimekiri salvestatud (lisatud faili lõppu).")