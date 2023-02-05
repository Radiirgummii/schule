def neuer_datensatz():
  # Hier kommt der Code für das Hinzufügen eines neuen Datensatzes
  print("Neuer Datensatz wurde hinzugefügt")

def daten_anzeigen():
  # Hier kommt der Code für das Anzeigen der Daten
  print("Daten werden angezeigt")

def daten_korrigieren():
  # Hier kommt der Code für das Korrigieren der Daten
  print("Daten werden korrigiert")

def daten_löschen():
  # Hier kommt der Code für das Löschen der Daten
  print("Daten werden gelöscht")

# Dictionary mit den Auswahloptionen und den entsprechenden Funktionen
optionen = {
  1: neuer_datensatz,
  2: daten_anzeigen,
  3: daten_korrigieren,
  4: daten_löschen
}

# Hauptschleife zum Einlesen der Benutzereingaben und Ausführen der Funktionen
while True:
  # Benutzereingabe einlesen
  print("""
  1: neuer_datensatz
  2: daten_anzeigen
  3: daten_korrigieren
  4: daten_löschen
  0: beenden
  """)
  auswahl = int(input("Bitte geben Sie die gewünschte Auswahlziffer ein: "))

  # Wenn der Benutzer 0 eingibt, beenden wir die Schleife und damit das Programm
  if auswahl == 0:
    break

  # Aufruf der entsprechenden Funktion aus dem Dictionary
  try:
    optionen[auswahl]()
  except KeyError:
    print(f"{auswahl} is not a valid option")