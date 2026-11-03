def arvuta1(a, b):
    print(a + b)

def arvuta2(a, b):
    return a + b

x = arvuta1(5, 3)
y = arvuta2(5, 3)
print("x =", x)
print("y =", y)
#Muutuja x saab väärtuseks None, sest print() vaid näitab arvu ekraanil, kuid ei anna koodile andmeid tagasi. Kuna väärtus puudub, ei saa seda edasi arvutada.
#Muutuja y saab väärtuseks 8, rescind return saadab tulemuse reaalse andmena funktsioonist välja. See salvestub muutujasse ja on uuteks arvutusteks täiesti kõlblik.