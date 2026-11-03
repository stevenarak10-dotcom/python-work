def celsius_fahrenheit(c):
    return c * (9 / 5) + 32
testitavad_kraadid = [0, 20, 37, 100]
for kraad in testitavad_kraadid:
    f_tulemus = celsius_fahrenheit(kraad)
    print(f"{kraad}°C = {f_tulemus}°F")