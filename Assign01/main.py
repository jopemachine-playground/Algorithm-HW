from Assign01.mergeSort import merge_sort
from Assign01.insertionSort import insertion_sort

def test_insertionSort(source, dest):
    try:
        fr = open(source, 'r')
        inputStr = fr.readline();
        inputArr = list(map(int, inputStr.split(',')))

        insertion_sort(inputArr);

        fw = open(dest, 'w')

        for i in range(0, len(inputArr) - 1, 1):
            fw.write(str(inputArr[i]) + ",")

        fw.write(str(inputArr[len(inputArr) - 1]))

    except FileNotFoundError:
        print ("test File Not Found!")

def test_mergeSort(source, dest):
    try:
        fr = open(source, 'r')
        inputStr = fr.readline();
        inputArr = list(map(int, inputStr.split(',')))

        merge_sort(inputArr)

        fw = open(dest, 'w')

        for i in range(0, len(inputArr), 1):
            fw.write(str(inputArr[i]) + ",")
        fw.write(str(merge_sort.counter))

    except FileNotFoundError:
        print ("test File Not Found!")


if __name__ == "__main__":
    source_data                 = "data/data02.txt"
    insertion_sort_dest_data    = "data/hw01_05_201502085_insertion.txt"
    merge_sort_dest_data        = "data/hw01_05_201502085_merge.txt"

    test_insertionSort(source_data, insertion_sort_dest_data)
    test_mergeSort(source_data, merge_sort_dest_data)
