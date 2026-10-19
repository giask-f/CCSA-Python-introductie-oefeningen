
rood_wit = int(input())
wit_blauw = int(input())
operator = input()

for blauw in range(2, wit_blauw-1):
    wit = wit_blauw - blauw
    rood = rood_wit - wit

    if rood < 2 or wit < 2 or blauw < 2:
        continue

    if operator == "<" and blauw + rood < wit_blauw:
        print(blauw)
        print(wit)
        print(rood)
        break
    elif operator == ">" and blauw + rood > wit_blauw:
        print(blauw)
        print(wit)
        print(rood)
        break

