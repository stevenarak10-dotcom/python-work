oige_parool = "python123"
katsed = 3

while katsed > 0:
    sisestus = input("Sisesta parool: ")
    
    if sisestus == oige_parool:
        print("Ligipääs lubatud!")
        break
    else:
        katsed -= 1
        if katsed > 0:
            print("Vale parool!")
            print()
if katsed == 0:
    print("Ligipääs blokeeritud!")
