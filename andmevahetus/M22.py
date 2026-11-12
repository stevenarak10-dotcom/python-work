from urllib.request import urlopen

url = "https://w3.org"

with urlopen(url) as vastus:
    baidid = vastus.read()
    tekst = baidid.decode("utf-8")
    print(tekst)