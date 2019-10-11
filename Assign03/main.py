from Assign03.closestPoint import *
from Assign03.inversion import *

if __name__ == "__main__":
    source_data_closest         = "data03/data03_closest.txt"
    source_data_inversion       = "data03/data03_inversion.txt"

    try:
        fr = open(source_data_inversion, 'r')
        inputStr = fr.readline();
        inputArr = list(map(int, inputStr.split(',')))
        count, res = sort_and_count(inputArr)
        print(count)
    except FileNotFoundError:
        print("test File Not Found!")

    try:
        fr = open(source_data_closest, 'r')
        array_list = []
        while True:
            inputStr = fr.readline()
            if not inputStr:
                break
            elem = list(map(float, inputStr.split(',')))
            array_list.append(elem)
        print(closest_pair(array_list))

    except FileNotFoundError:
        print("test File Not Found!")

    # test_insertionSort(source_data, insertion_sort_dest_data)
    # test_mergeSort(source_data, merge_sort_dest_data)
