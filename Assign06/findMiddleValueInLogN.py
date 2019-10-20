def find_middle_value(arr1, arr2, n):

    if n == 1:
        if arr1[0] > arr2[0]:
            ret = arr2[0]
        else:
            ret = arr1[0]
        return ret

    elif n == 2:
        arr = arr1 + arr2
        arr.sort()
        return arr[1]

    else:

        middle_1 = arr1[int(n/2)]
        middle_2 = arr2[int(n/2)]

        # 중간값이 더 큰 배열의 중간값보다 더 큰 값들을 버린다.
        # 중간값이 작은 배열의 중간값보다 작은 값들을 같은 갯수만큼 버린다.
        # 결과적으로 base case에서 잘게 쪼개진 두 배열을 합쳐 중간값을 구하면 원래 구하려 했던 중간값이 구해진다.
        if middle_1 > middle_2:

            if n % 2 == 0:
                return find_middle_value(arr1[:int(n / 2) + 1], arr2[int(n / 2) - 1:], int(n / 2) + 1)
            else:
                return find_middle_value(arr1[:int(n / 2) + 1], arr2[int(n / 2):]    , int(n / 2) + 1)

        else:
            if n % 2 == 0:
                return find_middle_value(arr1[int(n / 2 - 1):], arr2[:int(n / 2 + 1)], int(n / 2) + 1)
            else:
                return find_middle_value(arr1[int(n / 2):]    , arr2[:int(n / 2) + 1], int(n / 2) + 1)



if __name__ == "__main__":

    source_data1                = "data06_a.txt"
    source_data2                = "data06_b.txt"

    try:

        fr1 = open(source_data1, 'r')
        fr2 = open(source_data2, 'r')
        array1Str = fr1.readline()
        array2Str = fr2.readline()

        inputArr1 = list(map(int, array1Str.split(',')))
        inputArr2 = list(map(int, array2Str.split(',')))
        # inputArr1 = [1, 5, 6, 7]
        # inputArr2 = [2, 3, 4, 8]

        print(find_middle_value(inputArr1, inputArr2, len(inputArr1)))

    except FileNotFoundError:
        print("test File Not Found!")
