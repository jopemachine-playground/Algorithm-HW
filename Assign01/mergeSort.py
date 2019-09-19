def merge(collection, first, middle, last):

    # 아래와 같이 카운터 변수를 함수에 바인딩 할 수 있고,
    # 함수에 바인딩된 변수를 main.py에서 사용할 수 있다.
    merge_sort.counter += 1
    # 길이가 최대 배열의 길이와 같은 비어 있는 배열을 생성
    temp = [None] * len(collection)

    left_first = first
    left_last = middle

    right_first = middle + 1
    right_last = last

    index = left_first

    while left_first <= left_last and right_first <= right_last:

        if collection[left_first] < collection[right_first]:
            temp[index] = collection[left_first]
            left_first += 1
        else:
            temp[index] = collection[right_first]
            right_first += 1

        index += 1

    while left_first <= left_last:
        temp[index] = collection[left_first]
        left_first += 1
        index += 1

    while right_first <= right_last:
        temp[index] = collection[right_first]
        right_first += 1
        index += 1

    for index in range(first, last + 1, 1):
        collection[index] = temp[index]

    return

def split(collection, first, last):
    if first < last:
        middle_pivot = (int)((first + last) / 2);
        split(collection, first, middle_pivot)
        split(collection, middle_pivot + 1, last)
        merge(collection, first, middle_pivot, last)
    return


def merge_sort(collection):
    split(collection, 0, len(collection) - 1)

merge_sort.counter = 0

if __name__ == "__main__":
    arr = [1381,20144,2937,8401,31904,22750,27539,6615,1492,8110,12833,11891,25449,14327,19563,21346,16756,16012,16590,7966,8155,10696,2560,18444,10171,22890,14236,21239,28678,22691,30682,1469,30065,1646,28317,29256,18829,6176,32180,11712,15667,10816,25177,2047,2598,21400,19454,22342,16372,28300]
    merge_sort(arr)

    for elem in arr:
        # end 옵션을 이용해 linefeed를 다른 문자로 변경
        print(str(elem), end=',')

    print(str(merge_sort.counter))
