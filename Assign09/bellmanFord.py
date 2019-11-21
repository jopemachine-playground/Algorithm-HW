if __name__ == "__main__":
    # 일반 그래프
    source_data1 = "data11_bellman_ford_1.txt"
    # 음수 사이클을 포함하는 그래프
    source_data2 = "data11_bellman_ford_2.txt"

    try:
        allItems = list()

        fr = open(source_data2, 'r')

        line = fr.readline()

        pointCnt = len(line.split(","))

        # pointCnt를 통한 이차원 배열 생성

        arr = [[float("inf")] * pointCnt for i in range(0, pointCnt)]
        dp = [float("inf")] * pointCnt

        while True:
            line = fr.readline()
            if not line:
                break

            onelineList = line.split(",")

            start = int(onelineList[0])
            end = int(onelineList[1])
            weight = int(onelineList[2])

            arr[start][end] = weight

        dp[0] = 0

        hasMinusCycle = False

        for i in range(0, pointCnt):
            print("-" * 10 + "iteration " + str(i) + "-" * 10)

            for u in range(0, pointCnt):
                for v in range(0, pointCnt):
                    if u != v and arr[u][v] != float("inf"):
                        if dp[v] > dp[u] + arr[u][v]:
                            print("Update distance of " + str(v) + " from " + str(dp[v]) + " to " + str(dp[u] + arr[u][v]))
                            dp[v] = dp[u] + arr[u][v]
                            if i == pointCnt - 1:
                                hasMinusCycle = True

            print("iteration " + str(i) + " distance : " + str(dp))

    except FileNotFoundError:
        print("test File Not Found!")

    if hasMinusCycle:
        print("The graph has nagative cycle")
