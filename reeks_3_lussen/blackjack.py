som = 0

while True:
    n = int(input())
    som += n
    if som == 21:
        print("Gewonnen!")
        break
    elif som > 21:
        print(f"Verbrand ({som})")
        break
    elif n == 0:
        print(f"Voorzichtig gespeeld ({som})")
        break
