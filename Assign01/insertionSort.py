def insertion_sort(collection):
    for i in range(1, len(collection), 1):
        for j in range(i, 0, -1):
            if collection[j-1] > collection[j]:
                collection[j-1], collection[j] = collection[j], collection[j-1]


if __name__ == "__main__":
    arr = [88, 33, 222, 77, 11, 33, 0, 99, 33, 66]
    insertion_sort(arr)

    for elem in arr:
        # end 옵션을 이용해 linefeed를 다른 문자로 변경
        print(str(elem), end=' ')
