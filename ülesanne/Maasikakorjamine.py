def raha_eurodes(ämbri_arv,kilohind):
    return round(ämbri_arv * 5 * kilohind/100, 1)
failinimi = input("Sisesta failinimi: ")
kilohind = int(input("Sisesta kilo_hind sentides: "))
kokku = 0
with open(failinimi, "r", encoding="UTF-8") as f:
    kastid = f.readlines()
    for i, arv in enumerate(kastid):
        arv = int(arv.strip())
        raha = raha_eurodes(arv, kilohind)
        print(f"{i}. päeval sai {raha} eurot.")
        kokku += raha
print(f"Kokku teeniti {kokku} eurot.")