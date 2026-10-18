p = int(input())
k = int(input())

overgebleven_noten = k

def noten(aantal):
    if aantal == 0:
        return "geen noten"
    elif aantal == 1:
        return "1 noot"
    else:
        return f"{aantal} noten"

for i in range(1,p+1):
    aantal_noten = overgebleven_noten
    noten_piraat = overgebleven_noten // p
    noten_aap = overgebleven_noten % p
    overgebleven_noten = aantal_noten - noten_piraat - noten_aap
    print(f"{noten(aantal_noten)} = {noten(noten_piraat)} voor piraat#{i} en {noten(noten_aap)} voor de aap")

noten_piraat = overgebleven_noten // p
noten_aap = overgebleven_noten % p

print(f"elke piraat krijgt {noten(noten_piraat)} en {noten(noten_aap)} voor de aap")



