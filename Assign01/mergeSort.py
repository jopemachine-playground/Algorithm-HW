def merge(collection, first, middle, last):
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


if __name__ == "__main__":
    arr = [88, 33, 222, 77, 11, 33, 0, 99, 33, 66]
    merge_sort(arr)

    for elem in arr:
        # end 옵션을 이용해 linefeed를 다른 문자로 변경
        print(str(elem), end=' ')
