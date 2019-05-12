import pysnooper

@pysnooper.snoop()
def main():
    n, a, b = map(int, input().split())

    sum = 0
    for i in range(1, n+1):
        digit_sum = 0
        num = i
        while(num > 0):
            digit_sum += num % 10
            num //= 10

        if (digit_sum >= a) and (digit_sum <= b):
            sum += i

    print(sum)


if __name__ == "__main__":
    main()
