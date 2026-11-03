otsitav = input("Sisesta toode: ").strip().lower()

leitud = False

with open('tooted.txt', 'r', encoding='utf-8') as fail:
    for rida in fail:
        toode = rida.strip().lower()
        
        if toode == otsitav:
            leitud = True
            break

if leitud:
    print("Toode leiti nimekirjast.")
else:
    print("Toodet ei leitud nimekirjast.")