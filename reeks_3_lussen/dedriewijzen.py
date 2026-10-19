t = round(float(input()) * 100)

gevonden = False

for a in range(1, t + 1):
    if gevonden:
        break

    for b in range(a, t + 1):
        c = t - a - b

        if c < b:
            break

        if a * b * c == t * 10000:
            print(f"€{a / 100:.2f} + €{b / 100:.2f} + €{c / 100:.2f} = €{a / 100:.2f} x €{b / 100:.2f} x €{c / 100:.2f} = €{t / 100:.2f}")
            gevonden = True
            break