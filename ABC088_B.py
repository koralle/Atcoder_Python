import pysnooper

@pysnooper.snoop()
def main():
    n = int(input())
    a = [int(x) for x in input().split()]

    a.sort(reverse = True)

    Alice, Bob = 0, 0

    for turn in range(0, len(a), 2):
        Alice += a[turn]

    for turn in range(1, len(a), 2):
        Bob += a[turn]

    print(Alice - Bob)

if __name__ == "__main__":
    main()
