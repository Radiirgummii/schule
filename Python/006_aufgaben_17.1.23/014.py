def main():
    gl = float(input("Grundstückslänge(m): "))
    gb = float(input("Grundstücksbreite(m): "))
    m2p = float(input("m^2 preis(€): "))
    mprov_rel = float(input("Marklerprovision_relativ(%): "))/100
    u_str = float(input("Umsatzsteuer(%): "))/100

    grund_preis = gl * gb * m2p * (1 - u_str)
    marklerprovision_absolut = grund_preis * mprov_rel
    gesamt_grund_preis = grund_preis - marklerprovision_absolut
    print(f"{marklerprovision_absolut = }\n{gesamt_grund_preis = }")


if __name__ == "__main__":
    main()