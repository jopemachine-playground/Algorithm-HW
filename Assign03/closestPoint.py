from operator import itemgetter


def closest_pair(_list):
    # sort by X
    _list.sort()
    # brute force
    if len(_list) <= 3:
        return brute_force_closest_pair(_list)

    # Divide
    middle_x_index = (int) (len(_list) / 2)
    middle_x       = (_list[middle_x_index - 1][0] + _list[middle_x_index][0]) / 2

    sigma1 = closest_pair(_list[:middle_x_index])
    sigma2 = closest_pair(_list[middle_x_index:])
    sigma = min(sigma1, sigma2)

    # Delete less than sigma
    lessThanSigmaList_X = list(filter(lambda elem: (elem[0] > middle_x - sigma) or (elem[0] < middle_x + sigma), _list))
    # sort by Y
    lessThanSigmaList_X.sort(key=itemgetter(1))

    for i in range(0, len(lessThanSigmaList_X)):
        for j in range(i + 1, len(lessThanSigmaList_X)):
            if lessThanSigmaList_X[i][1] - lessThanSigmaList_X[j][1] > sigma:
                continue
            sigma = min(sigma, dist(lessThanSigmaList_X[i], lessThanSigmaList_X[j]))

    return sigma


def brute_force_closest_pair(_list):

    distance = []

    for i in range(0, len(_list)):
        for j in range(i + 1, len(_list)):
            a = _list[i][0] - _list[j][0]
            b = (_list[i][1] - _list[j][1]) ** 2
            distance.append(dist(_list[i], _list[j]))

    return min(distance)


def dist(pointA, pointB):
    return (((pointA[0] - pointB[0]) ** 2) + ((pointA[1] - pointB[1]) ** 2)) ** 0.5


if __name__ == "__main__":

    source_data_closest         = "data03/data03_closest.txt"

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
        print ("test File Not Found!")
