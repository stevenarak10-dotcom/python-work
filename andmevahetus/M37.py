import os
import urllib.request
import urllib.error

# N\u00e4idis-URL (Project Gutenbergi vabavaraline tekstifail)
VEEBI_URL = "https://gutenberg.org"
ARHIIVIFAIL = "veebitekst_arhiiv.txt"
ARUANDEFAIL = "teksti_statistika.txt"

def hangi_tekst(url, arhiivifail):
    """Proovib lugeda teksti veebist. Ebaõnnestumisel loeb kohalikust arhiivifailist."""
    try:
        print(f"Laadin andmeid aadressilt: {url} ...")
        # Lisame User-Agent p\u00e4ise, et veebiserver p\u00e4ringut ei blokeeriks
        paring = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(paring, timeout=10) as vastus:
            tekst = vastus.read().decode("utf-8")
            
        # Salvestame (arhiveerime) saadud teksti kohalikku arvutisse
        with open(arhiivifail, "w", encoding="utf-8") as fail:
            fail.write(tekst)
        print(f"Andmed on edukalt veebist laetud ja salvestatud faili '{arhiivifail}'.")
        return tekst

    except (urllib.error.URLError, TimeoutError, Exception) as viga:
        print(f"Veebipäring ebaõnnestus ({viga}).")
        
        # Kontrollime, kas kohalik arhiivifail on olemas
        if os.path.exists(arhiivifail):
            print(f"Kasutan varem salvestatud kohalikku faili '{arhiivifail}'.")
            with open(arhiivifail, "r", encoding="utf-8") as fail:
                return fail.read()
        else:
            print("Viga! Kohalikku varukoopiat ei leitud ja veebist lugemine ebaõnnestus.")
            return None

def arvuta_ja_salvesta_statistika(tekst, aruandefail):
    """Arvutab teksti statistika ja kirjutab selle aruandefaili."""
    read = tekst.splitlines()
    ridade_arv = len(read)
    sonad = tekst.split()
    sonade_arv = len(sonad)
    tahemargid_kokku = len(tekst)
    tahemargid_tuhikuteta = len(tekst.replace(" ", "").replace("\n", "").replace("\r", ""))
    
    puhastatud_sonad = [s.strip(".,!?;:\"'()[]-") for s in sonad]
    pikim_sona = max(puhastatud_sonad, key=len) if puhastatud_sonad else ""

    aruanne = (
        "TEKSTI STATISTIKA ARUANNE\n"
        + "=" * 35 + "\n"
        + f"Ridade arv: {ridade_arv}\n"
        + f"Sõnade arv: {sonade_arv}\n"
        + f"Tähemärke kokku (koos tühikutega): {tahemargid_kokku}\n"
        + f"Tähemärke (ilma tühikuteta): {tahemargid_tuhikuteta}\n"
        + f"Pikim sõna: '{pikim_sona}' ({len(pikim_sona)} tähemärki)\n"
    )

    with open(aruandefail, "w", encoding="utf-8") as fail:
        fail.write(aruanne)
        
    print(f"\nStatistika on arvutatud ja salvestatud faili '{aruandefail}':\n")
    print(aruanne)

sisu = hangi_tekst(VEEBI_URL, ARHIIVIFAIL)
if sisu is not None:
    arvuta_ja_salvesta_statistika(sisu, ARUANDEFAIL)