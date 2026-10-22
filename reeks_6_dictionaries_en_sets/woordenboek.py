def vertaling_toevoegen(woord, vertaling_woord, woordenboek):
    woordenboek[woord] = vertaling_woord

def vertaling(woord, woordenboek):
    if woord not in woordenboek:
        return "???"
    else:
        return woordenboek[woord]


woordenboek = {}
vertaling_toevoegen('plerzs', 'vrouw', woordenboek)
vertaling_toevoegen('nirtu', 'bloem', woordenboek)
vertaling_toevoegen('klinzoj', 'dorst', woordenboek)
vertaling_toevoegen('tilza', 'hond', woordenboek)
vertaling_toevoegen('zraidi', 'tijd', woordenboek)

print(vertaling('tilza', woordenboek))

print(vertaling('guoles', woordenboek))

