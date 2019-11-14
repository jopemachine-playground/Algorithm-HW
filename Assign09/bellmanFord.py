if __name__ == "__main__":
    # 일반 그래프
    source_data1 = "data11_bellman_ford_1.txt"
    # 음수 사이클을 포함하는 그래프
    source_data2 = "data11_bellman_ford_2.txt"

    try:
        allItems = list()

        fr = open(source_data1, 'r')

        line = fr.readline()

        pointCnt = len(line.split(","))

        # pointCnt를 통한 이차원 배열 생성

        arr = [[None] * pointCnt for i in pointCnt]

        while True:
            line = fr.readline()
            if not line:
                break

            onelineList = line.split(",")

            start = onelineList[0]
            end = onelineList[1]
            weight = onelineList[2]

            arr[start][end] = weight

    except FileNotFoundError:
        print("test File Not Found!")
