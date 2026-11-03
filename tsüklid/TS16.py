oige_parool = "python123"

while True:
    # Küsib kasutajalt parooli sisestust
    sisestus = input("Sisesta parool: ")

    if sisestus == oige_parool:
        print("Ligipääs lubatud!")
        break
    else:
        print("Vale parool!")
        print()
