def p(x, y, i, j):

    if i >= len(x) or j >= len(y):
        return -1
    else:
        return 1 if x[i] == y[j] else 0


if __name__ == "__main__":

    x = "tcatagttaaca"
    y = "tcagaagtacc"

    lx = len(x)
    ly = len(y)

    q = 2

    a = [[0] * (ly + 1) for i in range(0, lx + 1)]
    for i in range(0, lx + 1):
        a[1][0] = i * q
    for i in range(0, ly + 1):
        a[0][i] = i * q
    for i in range(1, lx + 1):
        for j in range(1, ly + 1):

            a[i][j] = max(a[i][j-1] - q, a[i-1][j-1] + p(x, y, i, j), a[i-1][j] - q)

    print(a[lx][ly])

