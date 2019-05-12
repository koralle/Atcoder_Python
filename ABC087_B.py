def main():
    a = int(input())
    b = int(input())
    c = int(input())
    x = int(input())

    count = 0
    for ia in range(0, a+1):
        for jb in range(0, b+1):
            for kc in range(0, c+1):
                total = 500 * ia + 100 * jb + 50 * kc
                if total == x:
                    count += 1

    print(count)

if __name__ == "__main__":
    main()
