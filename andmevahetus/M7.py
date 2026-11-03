failinimi = input("Sisesta failinimi: ").strip()

try:
    with open(failinimi, 'r', encoding='utf-8') as fail:
        sisu = fail.read()
        print("\nFaili sisu:")
        print(sisu)

except FileNotFoundError:
    print("Viga: sellist faili ei leitud.")