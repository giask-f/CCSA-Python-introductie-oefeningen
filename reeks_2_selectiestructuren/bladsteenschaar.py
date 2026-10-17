speler1 = input()
speler2 = input()

wint_van = {
    "steen": ["hagedis", "schaar"],
    "schaar": ["blad", "hagedis"],
    "blad": ["steen", "Spock"],
    "hagedis": ["Spock", "blad"],
    "Spock": ["schaar", "steen"]
}

if speler1 == speler2:
    print("gelijkspel")
elif speler2 in wint_van[speler1]:
    print("speler1 wint")
else:
    print("speler2 wint")