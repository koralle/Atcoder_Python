def main():
    h, w = map(int, input().split())
    grid = []
    for height in range(0, h):
        grid.append(list(input()))

    dx = [0, 0, 1, 1, 1, -1, -1, -1]
    dy = [1, -1, 1, -1, 0, 1, -1, 0]

    for height in range(0, h):
        for width in range(0, w):
            if grid[height][width] == '#':
                continue
            else:
                grid[height][width] = 0

            for i in range(0, 8):
                if (height + dy[i] < 0) or (height + dy[i] >= h) or (width + dx[i] < 0) or (width + dx[i] >= w):
                    continue
                if (grid[height + dy[i]][width + dx[i]]) == '#':
                    grid[height][width] += 1

    for height in range(0, h):
        for width in range(0, w):
            print(grid[height][width], end='')
        print()


if __name__ == "__main__":
  main()
