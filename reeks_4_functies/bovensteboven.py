def bovensteboven(n):

    cijfers = str(n)
    draai = {"0" : "0", "1" : "1", "6" : "9", "8" : "8", "9" : "6"}

    resultaat = ""

    for cijfer in cijfers:
        if cijfer not in draai:
            return False
        resultaat = draai[cijfer] + resultaat

    return resultaat == cijfers

def volgende(n):
    getal = n+1
    
    while not bovensteboven(getal):
        getal += 1
        
    return getal