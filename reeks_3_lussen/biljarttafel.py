h = int(input())
b = int(input())

x = 0
y = 0
dx = 1
dy = 1



while True:

    afstand_x = b - x if dx == 1 else x
    afstand_y = h - y if dy == 1 else y

    if afstand_x < afstand_y:
        x += dx * afstand_x
        y += dy * afstand_x
    elif afstand_x > afstand_y:
        x += dx * afstand_y
        y += dy * afstand_y
    else:
        x += dx * afstand_x
        y += dy * afstand_y



    if (x == 0 or x == b) and (y == 0 or y == h):
        if x == 0 and y == 0:
            print(f"linkeronderpocket ({x}, {y})")
        elif x == b and y == 0:
            print(f"rechteronderpocket ({x}, {y})")
        elif x == 0 and y == h:
            print(f"linkerbovenpocket ({x}, {y})")
        else:
            print(f"rechterbovenpocket ({x}, {y})")
        break

    if y == h:
        print(f"bovenband ({x}, {y})")
        dy = -1
    elif x == b:
        print(f"rechterband ({x}, {y})")
        dx = -1
    elif y == 0:
        print(f"onderband ({x}, {y})")
        dy = 1
    elif x == 0:
        print(f"linkerband ({x}, {y})")
        dx = 1

    
