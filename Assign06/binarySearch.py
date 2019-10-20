def binary_search(arr, start, end, target):

    while end >= start:

        middle_index = (start + end) / 2

        middle = arr[int(middle_index)]

        if middle == target:
            return True

        if target > middle:
            start = middle_index + 1
        elif target < middle:
            end = middle_index - 1

    return False


def binary_search_recursive(arr, start, end, target):
    if end < start:
        return False

    middle_index = (start + end) / 2

    middle = arr[int(middle_index)]

    if target == middle:
        return True

    if target > middle:
        return binary_search_recursive(arr, middle_index + 1, end, target)
    elif target < middle:
        return binary_search_recursive(arr, start, middle_index - 1, target)


if __name__ == "__main__":
    list_test = [88, 33, 222, 77, 11, 0, 99, 66, 33]
    list_test.sort()

    # True
    print(binary_search_recursive(list_test, 0, len(list_test) - 1, 88))
    print(binary_search_recursive(list_test, 0, len(list_test) - 1, 0))
    print(binary_search_recursive(list_test, 0, len(list_test) - 1, 33))

    # False
    print(binary_search_recursive(list_test, 0, len(list_test) - 1, 23))
    print(binary_search_recursive(list_test, 0, len(list_test) - 1, 98))
