parool = input("Sisesta parool: ")

pikkus = len(parool)

if pikkus < 8:
    print("liiga lühike")
elif pikkus <= 11:
    print("Parooli pikkus on sobiv.")
else:  # vähemalt 12 tähemärki
    print("pikk parool.")
