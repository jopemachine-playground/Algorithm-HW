def quick_sort(arr, comparator):
    sort(arr, 0, len(arr) - 1, comparator)


def sort(arr, first, last, comparator):
    if first < last:
        pivot_index = split(arr, first, last, comparator)
        sort(arr, first, pivot_index - 1, comparator)
        sort(arr, pivot_index + 1, last, comparator)


def split(arr, first, last):

    up_pointer = first
    down_pointer = last - 1
    pivot = arr[last]

    while up_pointer <= down_pointer:

        while pivot > arr[up_pointer]:
            up_pointer += 1
        while pivot <= arr[down_pointer]:
            down_pointer -= 1

        if up_pointer <= down_pointer:
            arr[up_pointer], arr[down_pointer] = arr[down_pointer], arr[up_pointer]

    arr[up_pointer], arr[last] = arr[last], arr[up_pointer]
    return up_pointer


def split_descend(arr, first, last):
    # 현재 같은 값은 정렬되지 않는 문제가 있음.
    up_pointer = first
    down_pointer = last - 1
    pivot = arr[last]

    while (up_pointer <= down_pointer):

        while (pivot <= arr[up_pointer]):
            up_pointer += 1
        while (pivot > arr[down_pointer]):
            down_pointer -= 1

        if (up_pointer <= down_pointer):
            arr[up_pointer], arr[down_pointer] = arr[down_pointer], arr[up_pointer]

    arr[up_pointer], arr[last] = arr[last], arr[up_pointer]
    return up_pointer


if __name__ == "__main__":
    list_test = [88, 33, 222, 77, 11, 33, 0, 99, 33, 66]
    quick_sort(list_test, lambda x, y: x < y)

    for i in list_test:
        print(i)
