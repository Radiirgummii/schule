def fac(n, e=0):
    e += n
    if n == 0:
        return e
    else:
        return fac(n-1, e)


def main():
    print(fac(int(input())))


if __name__ == "__main__":
    main()
