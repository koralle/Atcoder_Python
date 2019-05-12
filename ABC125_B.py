def main():
    N = int(input())
    V = [int(i) for i in input().split()]
    C = [int(i) for i in input().split()]

    sum = 0
    for i in range(0, len(V)):
        tmp = V[i] - C[i]
        if (tmp >= 0):
            sum += tmp

    print(sum)

if __name__ == "__main__":
    main()
