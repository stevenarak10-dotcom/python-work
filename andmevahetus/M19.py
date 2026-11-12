

with open("algtekst.txt", "w", encoding="utf-8") as fail:
    fail.write("See on algtekst, mis sisaldab nii suuri kui ka väikeseid tähti.\n")

with open("algtekst.txt", "r", encoding="utf-8") as algfail:
    sisu = algfail.read()
suurtähtedega_sisu = sisu.upper()

with open("suured_tahed.txt", "w", encoding="utf-8") as uus_fail:
    uus_fail.write(suurtähtedega_sisu)

print("Tekst on edukalt suurtähtedeks muudetud ja salvestatud faili suured_tahed.txt!")