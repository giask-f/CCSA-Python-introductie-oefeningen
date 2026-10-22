def iszigzag(r):
    teller = 0
    r = list(r)
    for cijfer in r:
        if teller == len(r)-1:
            break
        if teller % 2 == 0:
            if cijfer < r[teller + 1]:
                return False
        if teller % 2 != 0:
            if cijfer > r[teller + 1]:
                return False
        teller += 1

    return True


def zigzag_traag(r):
    r.sort()
    for i in range(0,len(r)-1,2):
        eerste_getal = r[i]
        tweede_getal = r[i+1]
        r[i] = tweede_getal
        r[i+1] = eerste_getal
    return r


def zigzag_snel(r):
    for i in range(0,len(r),2):

        if i == 0:
            getal1 = r[i]
            getal2 = r[i+1]

            if r[i] < r [i+1]:
                r[i] = getal2
                r[i+1] = getal1

        elif i == len(r)-1:
            getal1 = r[i]
            getal2 = r[i-1]
            
            if r[i] < r [i-1]:
                r[i] = getal2
                r[i-1] = getal1
        else:    

            if r[i] < r[i-1]:
                getal1 = r[i]
                getal2 = r[i-1]
                r[i] = getal2
                r[i-1] = getal1

            if r[i] < r[i+1]:
                getal1 = r[i]
                getal2 = r[i+1]
                r[i] = getal2
                r[i+1] = getal1



print(iszigzag([10,5,6,2,20,3,100,80]))
print(zigzag_traag([10,90,49,2,1,5,23]))
print(zigzag_snel([10,90,49,2,1,5,23]))
