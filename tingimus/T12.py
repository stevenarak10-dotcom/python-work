temp = float(input("Sisesta temperatuur: 30 "))

if temp < 0:
    print("Külmub")
elif temp <= 15:
    print("Jahe")
elif temp <= 25:
    print("Soe")
else:
    print("Palav")
