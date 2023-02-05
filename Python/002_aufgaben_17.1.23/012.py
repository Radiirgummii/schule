from statistics import mean

def main():
    zahlen = []
    for _ in range(4):
        zahlen.append(float(input("Zahl: ")))
    print(mean(zahlen))#mean() ermittelt den mittelwert aus allen zahlen einer liste

if __name__ == "__main__":
    main()