paaris_loendur = 0
paaritu_loendur = 0

with open('arvud.txt', 'r', encoding='utf-8') as fail:
    for rida in fail:
        arv = int(rida.strip())
        if arv % 2 == 0:
            paaris_loendur += 1
        else:
            paaritu_loendur += 1

print(f"Paarisarve: {paaris_loendur}")
print(f"Paarituid arve: {paaritu_loendur}")