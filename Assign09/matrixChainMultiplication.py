import sys


def mcm(p):
    n = len(p) - 1
    m = [[None] * (n + 1) for i in range(0, n + 1)]
    for i in range(1, n + 1):
        m[i][i] = 0
    for l in range(2, n + 1):
        for i in range(1, n - l + 2):
            j = i + l - 1
            m[i][j] = sys.maxsize
            for k in range(i, j):
                q = m[i][k] + m[k+1][j] + p[i-1] * p[k] * p[j]
                if q < m[i][j]:
                    m[i][j] = q
    return m


if __name__ == "__main__":

    source_data = "data11_matrix_chain.txt"
    arrSizeList = list()

    try:
        fr = open(source_data, 'r')

        while True:
            line = fr.readline()
            if not line:
                break

            onelineList = line.split(",")
            arrSizeList.append(int(onelineList[0]))
            lastValue = onelineList[1]

        arrSizeList.append(int(lastValue))
        m = mcm(arrSizeList)

        minMul = sys.maxsize
        for i in range(1, len(m)):
            for j in range(1, len(m)):
                if m[i][j] is not None and m[i][j] != 0 and minMul > m[i][j]:
                    minMul = m[i][j]
                print(m[i][j], end=' ')
            print()

        print()
        print("최소 곱셈의 수 : " + str(minMul))

    except FileNotFoundError:
        print("test File Not Found!")
