import pysnooper

@pysnooper.snoop()
def main():
    n = int(input())
    d = []

    for i in range(0, n):
        d.append(int(input()))

    backet = {}
    for i in range(0, 101):
        backet[i] = 0

    for i in range(0, n):
        backet[d[i]] += 1

    count = 0
    for i in range(0, 101):
        if backet[i] > 0:
            count += 1

    print(count)


if __name__ == "__main__":
    main()
