aantal_stuks = int(input())
kostprijs = float(input())
barcodes = int(input())
mijlen_per_coupon = int(input())

totaal_bedrag = aantal_stuks*kostprijs
mijlen = (aantal_stuks//barcodes)*mijlen_per_coupon

print(f"Phillips spendeerde ${totaal_bedrag} voor {mijlen} frequent flyer mijlen.")
