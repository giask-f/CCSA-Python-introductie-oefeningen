class Bankrekening:
    def __init__(self, naam_rekeninghouder, rekeningnummer, saldo):
        self.naam_rekeninghouder = naam_rekeninghouder
        self.rekeningnummer = rekeningnummer
        self.saldo = 0

    def __str__(self):
        s1 = self.naam_rekeninghouder
        s2 = str(self.rekeningnummer)
        s3 = str(self.saldo)

        return f"{s1}, {s2}, bedrag: {s3}"

    def __repr__(self):
        return f"Bankrekening('{self.naam_rekeninghouder}', {self.saldo})"

    def storten(self, n):
        self.saldo += n

    def afhalen(self, n):
        self.saldo -= n

b2 = Bankrekening('Peter Peeters', '001457894501', 10000)
print(repr(b2))