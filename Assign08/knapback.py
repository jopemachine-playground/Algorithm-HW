class Item:

    def __init__(self, value, weight):
        self.value = value
        self.weight = weight


# 원래 알고 있던 방법으로 푼 것
def pack(allItems, capacity, index):
    if index == pack.itemMaxNumber:
        return 0

    if pack.cache[capacity][index] != -1:
        return pack.cache[capacity][index]

    pack.cache[capacity][index] = pack(allItems, capacity, index + 1)

    if capacity >= allItems[index].weight:
        pack.cache[capacity][index] = max(pack.cache[capacity][index],
                                          pack(allItems,
                                               capacity - allItems[index].weight,
                                               index + 1) + allItems[index].value)

    return pack.cache[capacity][index]


# 의사코드를 이용해 짠 코드
def pack_2(allItems, capacity, index):
    if index == -1:
        return 0

    if pack_2.opt[index][capacity] != -1:
        return pack_2.opt[index][capacity]

    if allItems[index].weight > capacity:
        pack_2.opt[index][capacity] = pack_2(allItems, capacity, index - 1)
    else:
        v1 = pack_2(allItems, capacity, index - 1)
        v2 = allItems[index].value + pack_2(allItems, capacity - allItems[index].weight, index - 1)

        pack_2.opt[index][capacity] = max(v1, v2)

    return pack_2.opt[index][capacity]


def analysis(opt):
    ans = list()
    for i in range(0, item_cnt):
        for j in range(0, int(bag_size) + 1):
            if opt[i][j] == maxValue:
                ans.append(i)
    print(ans)


if __name__ == "__main__":

    source_data = "data09_knapsack.txt"

    print("배낭의 사이즈를 입력하세요 (0~50) : ")
    bag_size = input()

    try:
        item_cnt = -1
        allItems = list()

        fr = open(source_data, 'r')
        while True:
            item_cnt = item_cnt + 1
            line = fr.readline()
            if not line:
                break
            index, value, weight = line.split(",")
            allItems.append(Item(int(value), int(weight)))

        pack_2.selectItem = list()
        pack_2.opt = [[-1] * (int(bag_size) + 1) for i in range(0, item_cnt + 1)]

        # 테이블에 있는 값들 출력
        for i in range(0, item_cnt):
            for j in range(0, int(bag_size) + 1):
                print(str(pack_2(allItems, j, i)), end='    ')
            print()

        pack_2.selectItem = list()
        pack_2.opt = [[-1] * (int(bag_size) + 1) for i in range(0, item_cnt + 1)]

        # 주어진 knapback 문제를 풀고 max 값을 찾아냄
        maxValue = pack_2(allItems, int(bag_size), int(item_cnt) - 1);
        print("max : " + str(maxValue))

        # 주어진 문제에서 고른 item 들을 찾아 출력
        analysis(pack_2.opt)

    except FileNotFoundError:
        print("test File Not Found!")


