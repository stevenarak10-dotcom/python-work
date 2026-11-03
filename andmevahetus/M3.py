with open('nimed.txt', 'r', encoding='utf-8') as fail:
    loendur = 0
    for rida in fail:
        loendur += 1
print(f"Failis on {loendur} nime.")