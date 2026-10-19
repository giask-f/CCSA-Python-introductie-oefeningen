def even_oneven(getal):
    cijfers = list(str(getal))
    teller_even = 0
    teller_oneven = 0

    for cijfer in cijfers:
        if int(cijfer) % 2 == 0:
            teller_even += 1
        else:
            teller_oneven += 1
    
    return (teller_even,teller_oneven)

def volgende(getal):
    lijst = even_oneven(getal)

    resultaat = str(lijst[0]) + str(lijst[1]) + str(len(list(str(getal))))
    return int(resultaat)


def stappen(getal):
    teller = 0

    while getal != 123:
        getal = volgende(getal)
        teller += 1
    
    return teller
            