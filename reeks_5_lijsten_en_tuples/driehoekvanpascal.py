import math

def driehoek(r):

    assert isinstance(r, int) and not isinstance(r, bool) and r >= 0, \
        "ongeldig aantal rijen"

    rijen = []
    for i in range (0, r):
        if i == 0:
            rijen.append([1])
        elif i == 1:
            rijen.append([1,1])
        else:
            rij = [1]

            for j in range(1,len(rijen[i-1])):
                rij.append(rijen[i-1][j-1] + rijen[i-1][j])

            rij.append(1)
            rijen.append(rij)
    return rijen

def zeshoek(a,b):
    x = a-1
    y = b-1

    rijen = driehoek(x+2)

    assert 1 <= x < len(rijen) - 1 and \
           1 <= y < len(rijen[x]) - 1, \
           "ongeldige interne positie"

    return [rijen[x-1][y-1], rijen[x-1][y], rijen[x][y+1], rijen[x+1][y+1], rijen[x+1][y], rijen[x][y-1]]

def kwadraat(x,y):
    cijfers = zeshoek(x,y)
    string1 = f"{cijfers[0]} x {cijfers[1]} x {cijfers[2]} x {cijfers[3]} x {cijfers[4]} x {cijfers[5]}"
    string2 = f"{math.prod(cijfers)}"
    string3 = f"{math.prod(cijfers)**0.5:.0f} x {math.prod(cijfers)**0.5:.0f}"
    return f"{string1} = {string2} = {string3}"


print(driehoek(0))
print(zeshoek(8,4))
print(kwadraat(8,4))




