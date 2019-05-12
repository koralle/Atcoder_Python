import pysnooper

@pysnooper.snoop()
def main():
    a, b, x = map(int, input().split())

    result = 0
    if a % x == 0:
        result = (b // x) - (a // x) + 1
    else:
        result = (b // x) - (a // x)

    print(result)

if __name__ == "__main__":
    main()
