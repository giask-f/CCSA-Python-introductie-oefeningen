x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x3 = int(input())
y3 = int(input())
x4 = int(input())
y4 = int(input())


if max(x1, x2) > min(x3, x4) and max(x3, x4) > min(x1, x2) and max(y1, y2) > min(y3, y4) and max(y3, y4) > min(y1, y2):
    print("botsing")
else:
    print("geen botsing")