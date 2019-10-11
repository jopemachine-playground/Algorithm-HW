def sort_and_count(_list):
    if len(_list) == 1:
        return (0, _list)

    subList_A = _list[: (int)(len(_list) / 2)]
    subList_B = _list[((int)(len(_list) / 2)):]

    rA, A = sort_and_count(subList_A)
    rB, B = sort_and_count(subList_B)
    r , L = merge_and_count(A, B)
    r     = rA + rB + r
    return (r, L)


def merge_and_count(A, B):

    inversion_count = 0
    indexA = 0
    indexB = 0
    L = []

    Acount = len(A)
    Bcount = len(B)
    # 한 쪽이 0이 될 때 까지 진행
    while(Acount != 0 and Bcount != 0):
        if(A[indexA] > B[indexB]):
            inversion_count += Acount
            # L = B[indexB]
            L.append(B[indexB])
            indexB += 1
            Bcount -= 1
        else:
            # L = A[indexA]
            L.append(A[indexA])
            indexA += 1
            Acount -= 1

    while(Acount != 0):
        L.append(A[indexA])
        indexA += 1
        Acount -= 1

    while(Bcount != 0):
        L.append(B[indexB])
        indexB += 1
        Bcount -= 1

    return (inversion_count, L)


if __name__ == "__main__":

    source_data_inversion       = "data03/data03_inversion.txt"

    try:
        fr = open(source_data_inversion, 'r')
        inputStr = fr.readline();
        inputArr = list(map(int, inputStr.split(',')))
        count, res = sort_and_count(inputArr)
        print(count)
    except FileNotFoundError:
        print("test File Not Found!")
