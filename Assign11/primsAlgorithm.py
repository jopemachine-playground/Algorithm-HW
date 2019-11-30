from queue import PriorityQueue

if __name__ == "__main__":

    Q = PriorityQueue()

    map = [
        [ 0, 4,-1,-1,-1,-1,-1, 8,-1],
        [ 4, 0, 8,-1,-1,-1,-1,11,-1],
        [-1, 8, 0, 7,-1, 4,-1,-1, 2],
        [-1,-1, 7, 0, 9,14,-1,-1,-1],
        [-1,-1,-1, 9, 0,10,-1,-1,-1],
        [-1,-1, 4,14,10, 0, 2,-1,-1],
        [-1,-1,-1,-1,-1, 2, 0, 1, 6],
        [ 8,11,-1,-1,-1,-1, 1, 0, 7],
        [-1,-1, 2,-1,-1,-1, 6, 7, 0]
    ]

    numToAlpha = {0: "a", 1: "b", 2: "c", 3: "d", 4: "e", 5: "f", 6: "g", 7: "h", 8: "i"}

    key = [float("Inf")] * len(map)
    pi = [0] * len(map)

    # start point's weight equals zero
    key[0] = 0

    Q.put(0)

    visited = [False] * len(map)

    log = list()

    while not Q.empty():
        u = Q.get()

        visited[u] = True

        # adj(u)
        for i in range(0, len(map)):

            if map[u][i] == -1:
                continue

            if not visited[i] and map[u][i] < key[i]:
                key[i] = map[u][i]
                pi[i] = u
                Q.put(i)
                log.append([u, i, map[u][i]])

    for i in range(0, len(log)):
        print("w<" + numToAlpha.get(log[i][0]) + "," + numToAlpha.get(log[i][1]) + "> = " + str(log[i][2]))

    print()
    print("w<MST> = " + str(sum(key)))


