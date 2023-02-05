def main():
    gewicht = float(input("Gewicht: "))
    groesse = float(input("Größe: "))
    geschlecht = float(input("Geschlecht(m/w): "))
    bmi = gewicht / groesse ** 2
    
    if bmi < 19 and geschlecht == "w" or bmi < 20 and geschlecht == "m":
        print("untergewichtig")
    elif bmi > 24 and geschlecht == "w" or bmi > 25 and geschlecht == "m":
        print("übergewichtig")
    else:
        print("normalgewichtig")

if __name__ == "__main__":
    main()