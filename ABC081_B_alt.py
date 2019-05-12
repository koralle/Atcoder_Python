def main():
    n = int(input())
    a = [int(x) for x in input().split()]

    min = 1000000000
    for idx in range(0, len(a)):
        count = 0
        while(a[idx] % 2 == 0):
            a[idx] /= 2
            count += 1

        if count < min:
            min = count

    print(min)

if __name__ == "__main__":
    main()
