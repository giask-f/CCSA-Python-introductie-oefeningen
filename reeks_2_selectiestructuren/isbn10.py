som = 0


for i in range(9):
    som += int(input())*(i+1)

controlegetal = int(input())

if (som % 11) == controlegetal:
    print("OK")
else:
    print("FOUT")

