menge: float = float(input("menge: "))
preis: float = 8.99
# mengenabfrage
if 10 <= menge < 50:
    rabatt: float = 0.05
elif 50 <= menge < 100:
    rabatt = 0.07
elif 100 < menge:
    rabatt = 0.1
else:
    rabatt = 0

rechnung: float = menge * preis * (1 - rabatt)
print(f"ihre bestellung kostet {rechnung}")
if rechnung > 150:
    print("Glückwunsch, Sie bekommen eine Kiste Apfelsaft gratis!")
