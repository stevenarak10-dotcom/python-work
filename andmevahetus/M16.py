tooted = []

while True:
    toode = input("Sisesta toode: ")
    if toode == "STOP":
        break
    tooted.append(toode)

with open("ostunimekiri.txt", "w", encoding="utf-8") as fail:
    for toode in tooted:
        fail.write(toode + "\n")

print("\nOstunimekiri salvestatud.")