from random import *


def quick_sort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q-1)
        quick_sort(A, q+1, r)


def quick_sort_with_random(A, p, r):
    if p < r:
        q = randomized_partition(A, p, r)
        quick_sort(A, p, q-1)
        quick_sort(A, q+1, r)


def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range (p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    i += 1
    A[i], A[r] = A[r], A[i]
    return i


def randomized_partition(A, p, r):
    i = randint(p, r)
    A[r], A[i] = A[i], A[r]
    return partition(A, p, r)


if __name__ == "__main__":
    source_data                 = "data05.txt"
    dest_data                   = "hw03_05_201502085_quick.txt"
    dest_randomized_data        = "hw03_05_201502085_quickRandom.txt"

    try:
        fr = open(source_data, 'r')
        inputStr = fr.readline();
        inputArr1 = list(map(int, inputStr.split(',')))
        inputArr2 = list(map(int, inputStr.split(',')))

        quick_sort(inputArr1, 0, len(inputArr1) - 1)
        quick_sort_with_random(inputArr2, 0, len(inputArr2) - 1)

        fw      = open(dest_data, 'w')
        fw_rand = open(dest_randomized_data, 'w')

        for i in range(0, len(inputArr1) - 1, 1):
            fw.write(str(inputArr1[i]) + ",")

        for i in range(0, len(inputArr2) - 1 , 1):
            fw_rand.write(str(inputArr2[i]) + ",")

        fw.write(str(inputArr1[len(inputArr1) - 1]))
        fw_rand.write(str(inputArr2[len(inputArr2) - 1]))

    except FileNotFoundError:
        print("test File Not Found!")

