import string

letters = list(string.ascii_uppercase)

def codeer(t,s):
    tekst = list(t)
    gecodeerd = list()

    sleutel = (s * len(tekst))[:len(tekst)]
    
    for i in range(0,len(tekst)):
        if tekst[i]  not in letters:
            gecodeerd.append(tekst[i])
        else:
           cijfer_code = (letters.index(tekst[i]) + letters.index(sleutel[i])) % 26
           gecodeerd.append(letters[cijfer_code])

    resultaat = ""

    for code in gecodeerd:
            resultaat += code

    return resultaat


def decodeer(t,s):
    tekst = list(t)
    gedecodeerd = list()

    sleutel = (s * len(tekst))[:len(tekst)]
    
    for i in range(0,len(tekst)):
        if tekst[i]  not in letters:
            gedecodeerd.append(tekst[i])
        else:
           cijfer_code = (letters.index(tekst[i]) - letters.index(sleutel[i])) % 26
           gedecodeerd.append(letters[cijfer_code])

    resultaat = ""

    for code in gedecodeerd:
            resultaat += code

    return resultaat