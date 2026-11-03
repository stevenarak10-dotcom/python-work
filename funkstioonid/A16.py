def teisenda_sekundid(sekundid):
    tunnid = sekundid // 3600
    ylejaak = sekundid % 3600
    minutid = ylejaak // 60
    lõpu_sekundid = ylejaak % 60
    
    return (tunnid, minutid, lõpu_sekundid)

tulemus = teisenda_sekundid(3675)
print(f"Ennikuna: {tulemus}")

t, m, s = teisenda_sekundid(3675)
print(f"{t} tund(i), {m} minut(it) ja {s} sekund(it)")