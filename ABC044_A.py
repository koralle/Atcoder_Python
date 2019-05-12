def main():
    N = int(input())
    K = int(input())
    X = int(input())
    Y = int(input())

    if N <= K:
        print(X * N)
    else:
        print(X * K + (N - K) * Y)

if __name__ == "__main__":
    main()
