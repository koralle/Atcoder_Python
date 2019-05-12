def main():
    n = int(input())
    a = [int(x) for x in input().split()]

    count = 0
    while(True):
        for idx in range(0, len(a)):
            if a[idx] % 2 != 0:
                print(count)
                return
            a[idx] /= 2
        count += 1

if __name__ == "__main__":
    main()
