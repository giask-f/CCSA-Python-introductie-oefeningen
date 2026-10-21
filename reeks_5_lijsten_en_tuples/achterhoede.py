def zien(r):
    if isinstance(r,str):
        r = list(r) 

    hoeden_zien = []   
    teller = 0

    for item in r:
        if teller % 2 == 0:
            hoeden_zien.append('B')
        if teller % 2 != 0:
            hoeden_zien.append('R')
        if item == "R":
            teller += 1
    
    return tuple(hoeden_zien)

def zeggen(r):
    r = list(reversed(list(r)))

    dicta = {
    "R": "B",
    "B": "R"
    }

    hoeden_zeggen = []
    
    for i in range(0,len(r)):
        hoeden_zeggen.append(r[i])

        if r[i] == 'R':
            r = [dicta[x] for x in r]

    return tuple(reversed(hoeden_zeggen))



print(zien("BBRBRBRBBRBR"))
print(zeggen("BRRBR"))
