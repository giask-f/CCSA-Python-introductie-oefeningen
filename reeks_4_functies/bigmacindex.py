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
    wisselkoers_big_mac = prijs / KOSTPRIJS_BIG_MAC_AMERICA
    v = ((wisselkoers_big_mac - wisselkoers) / wisselkoers) * 100
    waardering = verhouding(v)
    return waardering

def wisselkoersanalyse(prijs, wisselkoers):
    return f"De {prijs.split()[1]} is {waardering(prijs.split()[0])} ten opzichte van de dollar."
    
    