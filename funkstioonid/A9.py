def ristkulik(laius, korgus):
    pindala = laius * korgus
    ymbermoot = 2 * (laius + korgus)
    print(f"Ristkülik mõõtmetega {laius}x{korgus}: Pindala = {pindala}, Ümbermõõt = {ymbermoot}")

print("--- Test 1 ---")
ristkulik(5, 10)

print("\n--- Test 2 ---")
ristkulik(3, 3)

print("\n--- Test 3 ---")
ristkulik(7.5, 4)