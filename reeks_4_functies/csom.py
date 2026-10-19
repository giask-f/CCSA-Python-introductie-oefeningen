def csom(x):
    cijfers = list(str(x))
    som = 0
    while True:
        for cijfer in cijfers:
            som += int(cijfer)
        if som < 10:
            return som
        
        cijfers = list(str(som))
        som = 0



        
