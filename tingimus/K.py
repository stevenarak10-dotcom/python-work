
nimi = input("Nimi: Steven ")
punktisumma = int(input("Punktisumma: 85 "))
puudumised = int(input("Puudumiste arv: 1 "))
tood_esitatud = input("Kas kõik tööd on esitatud (jah/ei):jah ")

print("Programm võiks väljastada:")
print(f"Õpilane: {nimi}")

if punktisumma >= 90:
    hinne = 5
elif punktisumma >= 75:
    hinne = 4
elif punktisumma >= 50:
    hinne = 3
elif punktisumma >= 20:
    hinne = 2
else:
    hinne = 1

print(f"Hinne: {hinne}")

if tood_esitatud == "jah":
    print("Kõik tööd on esitatud.")
else:
    print("Kõik tööd ei ole esitatud.")

if puudumised > 10 or tood_esitatud != "jah":
    if puudumised > 10:
        print("Hoiatus: Puudumisi on rohkem kui 10!")
else:
    print("Puudumiste arv on lubatud.")

if hinne >= 3 and puudumised <= 10 and tood_esitatud == "jah":
    print("Aine on läbitud.")
else:
    print("Aine ei ole läbitud.")
