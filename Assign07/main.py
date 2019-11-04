import numpy as np


def least_square_method(Xs: object, Ys: object) -> object:

    Xs_arr = np.zeros((len(Xs), 2))
    for i in range(0, len(Xs)):
        Xs_arr[i][0] = Xs[i]
        Xs_arr[i][1] = 1

    Ys_arr = np.zeros((len(Ys), 1))
    for i in range(0, len(Ys)):
        Ys_arr[i][0] = Ys[i]

    ATA    = np.matmul(np.transpose(Xs_arr), Xs_arr)

    # 역행렬이 존재하지 않는 경우도 처리하기 위해 Pseudo Inverse를 이용한다.
    ATAI   = np.linalg.pinv(ATA)
    ATAIAT = np.matmul(ATAI, np.transpose(Xs_arr))

    return np.matmul(ATAIAT, Ys_arr)


def segmented_least_squares(Xs, Ys, pointCnt, C):

    err = np.zeros((pointCnt, pointCnt))
    opt = np.zeros(pointCnt + 1)
    slicePoint = [()] * (pointCnt + 1)

    a_l_l = list(list())
    b_l_l = list(list())

    for j in range(0, pointCnt):

        a_l = list()
        b_l = list()

        for i in range(0, j):
            a, b = least_square_method(Xs[i:j + 1], Ys[i:j + 1])

            a_l.append(a)
            b_l.append(b)

            for k in range(i, j + 1):
                err[i, j] += (Ys[k] - (a[0] * Xs[k] + b[0])) ** 2

        a_l_l.append(a_l)
        b_l_l.append(b_l)

    for j in range(1, pointCnt + 1):

        opt[j], minP = min((err[i, j - 1] + C + opt[i], i) for i in range(j))

        slicePoint[j] = slicePoint[minP] + (minP,)

    final = slicePoint[-1] + (pointCnt,)

    print("Cost of the optimal solution : " + str(opt[-1]))
    print()
    print("An optimal solution : ")

    for i in range(0, pointCnt - 1):
        if i not in final:
            continue

        ind = final.index(i)

        print("[Segment " +
              str(i) +
              " - " +
              str(final[ind + 1]) +
              " : " + " y = " +
              str(a_l_l[final[ind + 1] - 1][i]) +
              " * x + " +
              str(b_l_l[final[ind + 1] - 1][i]) +
              "// square error: " +
              str(err[i][final[ind + 1] - 1]))


if __name__ == "__main__":

    source_data = "data07.txt"

    try:

        fr = open(source_data, 'r')
        arrayStr = fr.readline()

        inputArr = list(map(float, arrayStr.split(',')))

        pointCnt = inputArr[0]
        costValue = inputArr[len(inputArr) - 1]
        allPoint = inputArr[1:len(inputArr) - 1]
        Xs = allPoint[0::2]
        Ys = allPoint[1::2]
        segmented_least_squares(Xs, Ys, len(Xs), costValue)

    except FileNotFoundError:
        print("test File Not Found!")


