punktid = int(input("Sisesta punktid:82 "))
if punktid >= 90:
    hinne = 5
elif punktid >= 75:
    hinne = 4
elif punktid >= 50:
    hinne = 3
elif punktid >= 20:
    hinne = 2
else:
    hinne = 1
print(f"Hinne: {hinne}")
