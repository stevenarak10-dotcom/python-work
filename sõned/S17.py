sona = input("Sisesta sõna: ")

puhas_sona = sona.lower()

tagurpidi_sona = puhas_sona[::-1]

if puhas_sona == tagurpidi_sona:
    print("Tegemist on palindroomiga.")
else:
    print("See ei ole palindroom.")
