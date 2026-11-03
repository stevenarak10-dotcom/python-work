with open("tervitus.txt", "r", encoding="utf-8") as fail:
    for järjekorranumber, rida in enumerate(fail, start=1):
        print(f"{järjekorranumber}: {rida.strip()}")