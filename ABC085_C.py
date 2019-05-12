import pysnooper

@pysnooper.snoop()
def main():
    n, y = map(int, input().split())

    yukichi = 10000
    ichiyou = 5000
    hideyo  = 1000

    ans_x, ans_y, ans_z = -1, -1, -1
    for ix in range(0, n+1):
        for iy in range(0, n+1-ix):
            iz = n - ix - iy
            total = yukichi * ix + ichiyou * iy + hideyo * iz
            if total == y:
                ans_x, ans_y, ans_z = ix, iy, iz

    print(ans_x, ans_y, ans_z)


if __name__ == "__main__":
    main()
