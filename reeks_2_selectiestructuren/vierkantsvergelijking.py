import math

a = float(input())
b = float(input())
c = float(input())

d = b**2 - 4*a*c

if d < 0:
    print("geen wortels")
elif d == 0:
    print("een wortel")
    print(-(b/(2*a)))
else:
    print("twee wortels")
    x1 = (-b+math.sqrt(d))/(2*a)
    x2 = (-b-math.sqrt(d))/(2*a)
    print(min(x1,x2))
    print(max(x1,x2))

    
    
    