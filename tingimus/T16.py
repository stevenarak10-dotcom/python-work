vanus = int(input("Sisesta vanus: "))
if vanus < 18 or vanus >= 65:
    hind = 6
else:
    hind = 10
print(f"Pileti hind on {hind} eurot.")
