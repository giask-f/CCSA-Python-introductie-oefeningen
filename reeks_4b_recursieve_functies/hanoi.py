

def hanoi(n):
    def verplaats(n, bron, doel, hulp):
        if n == 1:
            print(f"Schijf 1 van {bron} naar {doel}")
        else:
            verplaats(n-1, bron, hulp,doel)
            print(f"Schijf {n} van {bron} naar {doel}")
            verplaats(n-1, hulp, doel, bron)

    verplaats(n, "A", "B", "C")
    print(f"{2**n-1} stappen gedaan")
        
        
hanoi(6)