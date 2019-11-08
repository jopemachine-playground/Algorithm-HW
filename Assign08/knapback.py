class Item:

    def __init__(self, value, weight):
        self.__value = value
        self.__weight = weight


def pack(allItems, cache, capacity, index, itemMaxNumber):
    if index == itemMaxNumber:
        return 0

    ret = cache[capacity][index]

    if ret != -1 :
        return ret

    ret = pack(allItems, cache, capacity, index + 1, itemMaxNumber)

    if capacity >= allItems[index].weight:
        ret = max(ret, pack(allItems, cache, capacity - allItems[index].weight, index + 1, itemMaxNumber) + allItems[index].value)

    return ret


if __name__ == "__main__":

    source_data = "data09_knapsack.txt"

    print("배낭의 사이즈를 입력하세요: ")
    bag_size = input()

    try:
        item_cnt = 0
        allItems = list()
        cache = list(list())
        fr = open(source_data, 'r')
        while True:
            item_cnt = item_cnt + 1
            line = fr.readline()
            if not line:
                break
            index, value, weight = line.split(",")
            allItems.append(Item(value, weight))
        print(pack(allItems, cache, bag_size, 0, item_cnt))

    except FileNotFoundError:
        print("test File Not Found!")


