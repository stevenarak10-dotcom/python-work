def esimene():
    print("A")
    print("B")

def teine():
    print("C")
    esimene()
    print("D")

print("Algus")
teine()
print("Lõpp")
#esimene() ja teine() on definitsioonid jäetakse alguseks
#print("Algus") käivitab rida
#ning teised lõpetavad töö read
#print("Lõpp") lõpetab koodi