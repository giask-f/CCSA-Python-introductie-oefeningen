prijs_boek = 24.95
korting_winkels = 0.4
prijs_versturen_eerste_boek = 3
prijs_versturen_boeken = 0.75
aantal_boeken_gekocht = 60

totaalprijs = (aantal_boeken_gekocht*prijs_boek) - (aantal_boeken_gekocht*prijs_boek)*korting_winkels + prijs_versturen_eerste_boek + prijs_versturen_boeken*(aantal_boeken_gekocht-1)

print(totaalprijs)