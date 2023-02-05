def main():
    y = float(input("Höhe: "))
    x = float(input("Breite: "))
    z = float(input("Länge: "))
    print(f"""
Volumen: {x * y * x}m³
Oberfläche: {2 * x * y + 2 * y * z + 2 * z * x}m²
Raumdiagonale: {(x ** 2 + y ** 2 + z ** 2) ** 0.5}
    """)

if __name__ == "__main__":
    main()