arvud = []
with open("arvud.txt", "r", encoding="utf-8") as fail:
    for rida in fail:

        rida = rida.strip()
        if rida:
              arvud.append(int(rida))

if arvud:
    suurim = max(arvud)
    väikseim = min(arvud)

    vahe = suurim - väikseim

    print(f"Suurim arv: {suurim}")
    print(f"Väikseim arv: {väikseim}")
    print(f"Vahe: {vahe}")
else:
    print("Fail on tühi või ei sisalda arve.")