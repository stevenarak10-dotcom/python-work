import string

parool = input("Sisesta parool: ")

erimargid = string.punctuation + " "

tingimused = [
    (len(parool) >= 8, "vähemalt kaheksat tähemärki"),
    (any(c.isupper() for c in parool), "vähemalt ühte suurtähte"),
    (any(c.islower() for c in parool), "vähemalt ühte väiketähte"),
    (any(c.isdigit() for c in parool), "vähemalt ühte numbrit"),
    (any(c in erimargid for c in parool), "erimärk")
]
punktid = 0
taitmata_tingimused = []

for tingimus_taitub, kirjeldus in tingimused:
    if tingimus_taitub:
        punktid += 1
    else:
        taitmata_tingimused.append(kirjeldus)

if punktid <= 2:
    hinnang = "Nõrk parool"
elif punktid <= 4:
    hinnang = "Keskmine parool"
else:
    hinnang = "Kõik nõuded täidetud"

print(f"\nTulemus: {punktid}/5")
print(f"Hinnang: {hinnang}")
if taitmata_tingimused:
    for tingimus in taitmata_tingimused:
        if tingimus == "erimärk":
            print("Puudub erimärk.")
        else:
            print(f"Puudub {tingimus}.")
