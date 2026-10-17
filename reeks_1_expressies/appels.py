aantal_stuks = int(input())

APPELS_PER_KIST = 20
KISTEN_PER_PALLET = 35

aantal_kisten = aantal_stuks // APPELS_PER_KIST
aantal_overgebleven_appels = aantal_stuks % APPELS_PER_KIST 

aantal_paletten = aantal_kisten // KISTEN_PER_PALLET
aantal_overgebleven_kisten = aantal_kisten % KISTEN_PER_PALLET

print(aantal_paletten)
print(aantal_overgebleven_kisten)
print(aantal_overgebleven_appels)