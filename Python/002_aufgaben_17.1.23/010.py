def main():
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))
    diskriminante = b ** 2 - 4 * a * b
    
    if diskriminante < 0:
        print("diskriminante ist negativ")
    elif diskriminante > 0:
        print("diskriminante ist positiv")
    else:
        print("diskriminante ist 0")

if __name__ == "__main__":
    main()