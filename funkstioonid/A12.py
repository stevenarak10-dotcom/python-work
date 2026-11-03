def kuva_hind(toode, hind, valuuta="€"):
    print(f"Toode: {toode} | Hind: {hind:.2f} {valuuta}")

kuva_hind("Klaviatuur", 35)
kuva_hind("Hiir", 20, "$")

kuva_hind("Peakomplekt", 49.99)