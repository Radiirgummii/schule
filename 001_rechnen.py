'''
zwei zahlen sollen miteinander verrechnet werden.
'''

#definitionen der zahlen
zahla: int = 1
zahlb: int = 2567

#rechungen
addition: int = zahla + zahlb
subtraktion: int = zahla - zahlb
multiplikation: int = zahla * zahlb


try:
    #versuchen zu dividieren
    division: float = zahla / zahlb
except ZeroDivisionError:  #falls die exeption ZeroDivisionError kommt fehlermeldung ausgeben und programm beenden
    print("division durch null ist nicht möglich")
    exit()
print(f"{zahla = }\n{zahlb = }\n{addition = }\n{subtraktion = }\n{multiplikation = }\n{division = :.2f}")
