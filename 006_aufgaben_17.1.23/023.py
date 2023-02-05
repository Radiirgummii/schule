def main():
    n = int(input())
    m = 1
    for i in range(n):
        print(f"{'*'*m : ^{n*2}}")
        m += 1

if __name__ == "__main__":
    main()