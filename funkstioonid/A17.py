import math
def ringi_pindala(raadius):
    return math.pi * (raadius ** 2)

raadiused = [3, 5.5, 10]
for r in raadiused:
    pindala = ringi_pindala(r)
    print(f"Ring raadiusega {r} -> Pindala = {pindala:.2f}")