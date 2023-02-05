import random

def main():
    a,b = (random.randint(1, 100), random.randint(1, 100))
    if int(input(f"{a}+{b}=")) == a+b:
        print("gut gemacht")
    print(a+b)
    





if __name__ == "__main__":
    main()