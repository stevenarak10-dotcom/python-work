ridade_arv = 0
mittetyhjade_ridade_arv = 0
sonade_koguarv = 0
tahemarkide_arv = 0
with open("tekst.txt", "r", encoding="utf-8") as fail:
    for rida in fail:
        ridade_arv += 1

        tahemarkide_arv += len(rida)

        if rida.strip():
            mittetyhjade_ridade_arv += 1

        sonad = rida.split()
        sonade_koguarv += len(sonad)

if ridade_arv > 0:
    keskmine_sonu_real = sonade_koguarv / ridade_arv
else:
    keskmine_sonu_real = 0
print("=== TEKSTI STATISTIKA ===")
print(f"Ridade arv kokku:         {ridade_arv}")
print(f"Mittetühjade ridade arv:  {mittetyhjade_ridade_arv}")
print(f"Sõnade arv kokku:         {sonade_koguarv}")
print(f"Tähemärkide arv:          {tahemarkide_arv}")
print(f"Keskmine sõnade arv real: {keskmine_sonu_real:.2f}")
print("=========================")