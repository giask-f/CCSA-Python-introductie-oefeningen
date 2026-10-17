kilometerteller_aanvang = float(input())
kilometerteller_inleveren = float(input())
benzine_te_tanken = float(input())

kilometers_gereden = kilometerteller_inleveren - kilometerteller_aanvang

benzine_verbruik = benzine_te_tanken/kilometers_gereden*100

print(benzine_verbruik)