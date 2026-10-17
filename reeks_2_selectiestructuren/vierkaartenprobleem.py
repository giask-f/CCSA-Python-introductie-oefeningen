soort = input()
kaart = input()
boolean = input()

if soort == "waarde":
    moet_draaien = int(kaart) % 2 == 0
else:
    moet_draaien = kaart != "rood"

if boolean == "ja":
    antwoord_correct = moet_draaien
else:
    antwoord_correct = not moet_draaien

if antwoord_correct:
    resultaat = "Juist"
else:
    resultaat = "Fout"

if moet_draaien:
    print(f"{resultaat}: kaarten met {soort} {kaart} moeten gedraaid worden.")
else:
    print(f"{resultaat}: kaarten met {soort} {kaart} moeten niet gedraaid worden.")

