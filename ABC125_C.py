
def main():
    n = int(input())
    a = [int(x) for x in input().split()]

    gcd_max = []
    l, r = 0, 0
    for idx in range(0, n):
        for idx_l in range(0, idx):
            if idx_l == 0:
                l = a[idx_l]
                continue
            l = gcd(l, a[idx_l])

        for idx_r in range(n-1, idx, -1):
            if idx_r == n-1:
                r = a[idx_r]
                continue
            r = gcd(r, a[idx_r])

        gcd_max.append(gcd(l, r))

    print(max(gcd_max))




def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    r = a % b
    return gcd(b, r)


if __name__ == "__main__":
    main()
