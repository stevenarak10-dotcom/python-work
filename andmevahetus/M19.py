laused = """Täna on ilus ja päikeseline ilm.
Mulle meeldib Pythonis programmeerida.
Koodi kirjutamine teeb meele rõõmsaks.
Failidega töötamine on tegelikult lihtne.
See on selle ülesande viies lause."""

with open("algtekst.txt", "w", encoding="utf-8") as fail:
    fail.write(laused)

with open("algtekst.txt", "r", encoding="utf-8") as algfail:
    sisu = algfail.read()
suurtähtedega_sisu = sisu.upper()

with open("suured_tahed.txt", "w", encoding="utf-8") as uus_fail:
    uus_fail.write(suurtähtedega_sisu)

print("Tekst on edukalt suurtähtedeks muudetud ja salvestatud faili suured_tahed.txt!")