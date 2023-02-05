# Initialisieren der Variablen
kapital = 5000. # Startkapital
zinsen = 0.03 # Zinssatz
jahre = 10 # Anzahl der Jahre

# Berechnen und Ausgeben des neuen Kapitals jedes Jahr
for jahr in range(1, jahre+1):
    kapital *= (1 + zinsen)
    print(f'Nach {jahr} Jahr(en) beträgt das neue Kapital {kapital:.2f} Euro.')
