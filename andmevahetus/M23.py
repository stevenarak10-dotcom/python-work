from urllib.request import urlopen

url = "https://w3.org"

with urlopen(url) as vastus:
    tekst = vastus.read().decode("utf-8")

read = tekst.splitlines()
sonad = tekst.split()
tyhjad_read = sum(1 for rida in read if rida.strip() == "")

print("Veebiteksti statistika")
print("--------")
print(f"Ridu: {len(read)}")
print(f"Sõnu: {len(sonad)}")
print(f"Tähemärke: {len(tekst)}")
print(f"Tühje ridu: {tyhjad_read}")
print()

print("Esimesed read:")
for nr, rida in enumerate(read[:10], start=1):
    print(f"{nr}. {rida}")