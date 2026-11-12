import re
from urllib.request import urlopen

url = "https://w3.org"
otsitav = input("Sisesta otsitav sõna: ").strip().lower()

with urlopen(url) as vastus:
    tekst = vastus.read().decode("utf-8")

sonad = re.findall(r"\b\w+\b", tekst.lower())
kogus = sonad.count(otsitav)

print(f"Otsitav sõna '{otsitav}' esineb tekstis {kogus} korda.")