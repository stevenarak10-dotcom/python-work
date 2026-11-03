parool = input("Sisesta parool:")
on_pikkus = len(parool)>= 8
on_suurtäht = False
on_väiketäht = False
on_väiketäht = False
on_number = False
on_erimärk = False

for märk in parool:
    if märk.isupper():
        on_suurtaht = True
    elif märk.islower():
        on_vaiketaht = True
    elif märk.isdigit():
        on_number = True
    elif not märk.isalnum():
        on_erimark = True

punktid = sum([on_pikkus, on_suurtaht, on_vaiketaht, on_number, on_erimark])

if punktid <= 2:
    hinnang = "Nõrk parool"
elif punktid <= 4:
    hinnang = "Keskmine parool"
else:
    hinnang = "Kõik nõuded täidetud"

print()
print(f"Tulemus: {punktid}/5")
print(f"Hinnang: {hinnang}")

if punktid < 5:
    print()
    if not on_pikkus:
        print("Puudub vähemalt 8 tähemärki.")
    if not on_suurtaht:
        print("Puudub suurtäht.")
    if not on_vaiketaht:
        print("Puudub väiketäht.")
    if not on_number:
        print("Puudub number.")
    if not on_erimark:
        print("Puudub erimärk.")