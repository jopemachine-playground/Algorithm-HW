from queue import PriorityQueue

if __name__ == "__main__":

    map = [
        [0, 10, 3,-1,-1],
        [10, 0, 1, 2,-1],
        [-1, 4, 0, 8, 2],
        [-1,-1,-1, 0, 7],
        [-1,-1,-1, 9, 0]
    ]

    numToAlpha = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E"}

    prev_d = [-1] * len(map)
    d = [-1] * len(map)

    pq = PriorityQueue()

    pq.put([0, 0])

    index = 0

    print("다익스트라 알고리즘으로 계산한 결과는 다음과 같습니다.")
    print("ㅡ" * 60)

    while pq.qsize() > 0:
        item = pq.get()
        cost = item[0]
        vertexID = item[1]

        if d[vertexID] != -1:
            continue

        d[vertexID] = cost

        res = ""

        res += ("-" * 110) + "\n"
        index += 1

        for i in range(0, len(map)):
            if map[vertexID][i] >= 0:

                totalCost = map[vertexID][i] + d[vertexID]

                if d[i] != -1:
                    res += "Q[" + str(i) + "] :" + "   d[" + numToAlpha[i] + "] = " + str(d[i]) + "\n"
                    continue

                res += "Q[" + str(i) + "] :" + "   d[" + numToAlpha[i] + "] = " + str(prev_d[i]) + " => " + "d[" + numToAlpha[i] + "] = " + str(totalCost) + "\n"

                prev_d[i] = totalCost

                pq.put([totalCost, i])

        print("S[" + str(index) + "]:    d[" + numToAlpha[vertexID] + "] = " + str(d[vertexID]))
        print(res)

        print("ㅡ" * 60)

    print("최종 결과: ")
    print(d)
