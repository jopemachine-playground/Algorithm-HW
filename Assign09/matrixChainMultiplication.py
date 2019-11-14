if __name__ == "__main__":
    source_data = "data11_matrix_chain.txt"

    arrSizeList = list()

    try:

        fr = open(source_data, 'r')

        line = fr.readline()

        pointCnt = len(line.split(","))

        # pointCnt를 통한 이차원 배열 생성
        arr = [[None] * pointCnt for i in pointCnt]

        while True:
            line = fr.readline()
            if not line:
                break

            onelineList = line.split(",")
            arrSizeList.append([onelineList[0], onelineList[1]])

    except FileNotFoundError:
        print("test File Not Found!")
