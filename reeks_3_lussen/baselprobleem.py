import math

som = 0

for i in range(1,101):
    som += 1/(i**2)
print(som)

teller = 1
som = 0

while True:
    som += 1/(teller**2)
    if abs(som - math.pi**2 / 6) <= 1/100:
        print(teller)
        break
    teller += 1
