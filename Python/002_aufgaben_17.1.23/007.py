def main():
    y = float(input("Höhe: "))
    x = float(input("Breite: "))
    z = float(input("Länge: "))
    if x < 0 or y < 0 or z < 0:
        print("negative Zahlen nind nicht zulässig")
    else: print(f"""
Volumen: {x * y * x}m³
Oberfläche: {2 * x * y + 2 * y * z + 2 * z * x}m²
Raumdiagonale: {(x ** 2 + y ** 2 + z ** 2) ** 0.5}
    """)

if __name__ == "__main__":
    main()