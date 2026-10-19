def ggd(a,b):
    x = max(a,b)
    y = min(a,b)
    z = x % y

    if z == 0:
        return y
    else:
        return ggd(y,z)

print(ggd(48,18))