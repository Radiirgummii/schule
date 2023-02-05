literpreis = float(input("Literpreis(€): "))
verbrauchte_liter = float(input("verbrauchte Liter(L): "))
gefahrene_km = float(input("gefahrene Strecke(km):"))

gesamtpreis = literpreis * verbrauchte_liter
verbrauch_p_100km = verbrauchte_liter / gefahrene_km / 10
preis_p_100km = verbrauch_p_100km * literpreis

print(f"{gesamtpreis = }\n{verbrauch_p_100km = }\n{preis_p_100km = :.f2}")