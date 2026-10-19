n = int(input())
teller = 0

for i in range(1,n):
    som = 0
    for j in range(i,n):
        som += j
        if som == n:
            teller += 1
        if som > n:
            break


print(teller)


