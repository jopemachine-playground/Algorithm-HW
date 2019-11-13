def p(x, y, i, j):
    return 1 if x[i] == y[j] else -1


if __name__ == "__main__":

    x = "tcatagttaaca"
    y = "tcagaagtacc"

    lx = len(x)
    ly = len(y)

    q = 2

    a = [[0] * (ly + 1) for i in range(0, lx + 1)]
    for i in range(0, lx + 1):
        a[i][0] = -1 * i * q
    for i in range(0, ly + 1):
        a[0][i] = -1 * i * q
    for i in range(1, lx + 1):
        for j in range(1, ly + 1):

            print("%" * 30)
            print("a1 :" + str(a[i][j-1] - q))
            print("a2 :" + str(a[i-1][j-1] + p(x, y, i-1, j-1)))
            print("a3 :" + str(a[i-1][j] - q))
            print("%" * 30)

            a[i][j] = max(a[i][j-1] - q, a[i-1][j-1] + p(x, y, i-1, j-1), a[i-1][j] - q)

        print("-" * 60)

