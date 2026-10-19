KOSTPRIJS_BIG_MAC_AMERICA = 4.07

def verhouding(v):
    if v <= -25:
        return "sterk ondergewaardeerd"
    if v <= -5:
        return "ondergewaardeerd"
    if v <= 5:
        return "ongeveer gelijk"
    if v <= 25:
        return "overgewaardeerd"
    return "sterk overgewaardeerd"

def waardering(prijs, wisselkoers):
    wisselkoers_big_mac = float(prijs) / KOSTPRIJS_BIG_MAC_AMERICA
    v = ((wisselkoers_big_mac - wisselkoers) / wisselkoers) * 100
    waardering = verhouding(v)
    return waardering

def wisselkoersanalyse(prijs, wisselkoers):
    prijzen = prijs.split()
    munteenheid = ""
    for i in range(1, len(prijzen)):
        if munteenheid == "":
            munteenheid += prijzen[i]
        else:
            munteenheid += " " + prijzen[i]

    
    return f"De {munteenheid} is {waardering(float(prijzen[0]),wisselkoers)} ten opzichte van de dollar."
    


print(waardering(3.44, 0.7))

print(wisselkoersanalyse("3.44 euro", 0.7))