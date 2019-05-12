def main():
    n = int(input())
    q = []
    for i in range(0, n):
        q.append([int(x) for x in input().split()])

    is_prime = eraatosthenes()

    a = []
    for i in range(0, 100000):
        a.append(0)

    for i in range(0, len(is_prime)):
        if i % 2 == 0:
            continue
        if is_prime[i] == 1 and is_prime[int((i + 1) / 2)] == 1:
            a[i] = 1

    s = [0]
    for i in range(0, len(a)):
        s.append(s[i] + a[i])

    for i in range(0, len(q)):
        l, r = q[i][0], q[i][1]
        print(s[r+1] - s[l])


def eraatosthenes():
    list = []
    for i in range(0, 100000):
        list.append(0)

    for i in range(2, len(list)):
        list[i] = 1

    for i in range(2, len(list)):
        if list[i] == 1:
            j = i * 2
            while j < len(list):
                list[j] = 0
                j += i
    return list

if __name__ == "__main__":
    main()
