if __name__ == "__main__":

    source_data = "data.txt"
    arrSizeList = list()

    try:
        fr = open(source_data, 'r')

        while True:
            line = fr.readline()
            if not line:
                break

            onelineList = line.split(",")
            arrSizeList.append(int(onelineList[0]))
            lastValue = onelineList[1]


    except FileNotFoundError:
        print("test File Not Found!")
