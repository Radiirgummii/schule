def main():
    a = int(input())
    i = 0
    while a >= 2**i:
        i+=1
    else:
        print(2**(i-1))
    


if __name__ == "__main__":
    main()