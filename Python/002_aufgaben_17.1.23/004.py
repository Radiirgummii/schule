def main():
    o_preis = float(input("Orginal Preis(€): "))
    rabatt = float(input("Rabatt(%): ")) / 100
    print(o_preis * (1 - rabatt))


if __name__ == "__main__":
    main()