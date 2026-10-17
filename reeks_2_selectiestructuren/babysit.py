beginuur = int(input())
beginminuut = int(input())
einduur = int(input())
eindminuut = int(input())

begin = beginuur * 60 + beginminuut
eind = einduur * 60 + eindminuut
if eind == 0:
    eind = 24*60

if begin < 18*60 or eind > 24*60 or eind <= begin:
    print("ongeldige invoer")
elif begin >= 21*60+30:
    uren_aan_tarief2 = (eind-begin)/60
    geld = uren_aan_tarief2*4
    print(geld)
elif eind <= 21*60+30:
    uren_aan_tarief1 = (eind-begin)/60
    geld = uren_aan_tarief1*2
    print(geld)
else:
    minuten_aan_tarief1 = (21*60+30) - begin
    uren_aan_tarief1 = minuten_aan_tarief1/60
    minuten_aan_tarief2 = eind - (21*60+30)
    uren_aan_tafief2 = minuten_aan_tarief2/60
    geld = uren_aan_tafief2*4 + uren_aan_tarief1*2
    print(geld)