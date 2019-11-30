from queue import PriorityQueue
import os


class Node:

    def __init__(self, alphabet, freq, left, right):

        self.alphabet = alphabet
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, rhs):
        return self.freq < rhs.freq

    def __le__(self, rhs):
        return self.freq <= rhs.freq

    def __gt__(self, rhs):
        return self.freq > rhs.freq

    def __ge__(self, rhs):
        return self.freq >= rhs.freq


def huffman_encode(pq, length):

    resDict = dict()

    for _ in range(1, length):
        x = pq.get()
        y = pq.get()

        z = Node(None, x.freq + y.freq, x, y)
        pq.put(z)

    root = pq.get()
    stk = list()
    stk.append([root, ""])

    while len(stk) != 0:

        root = stk.pop()
        rootNode = root[0]

        if rootNode.left != None:
            stk.append([rootNode.left, root[1] + "0"])

        if rootNode.right != None:
            stk.append([rootNode.right, root[1] + "1"])

        if rootNode.alphabet != None:
            resDict[rootNode.alphabet] = root[1]

    return resDict


def huffman_decode(C):
    pass


if __name__ == "__main__":

    # encoding input
    source_data = "data12.txt"

    # encoding output
    output_encoding = "hw12_05_201502085_encoded.txt"
    output_encoding_table = "hw12_05_201502085_encoded.txt"

    # decoding input
    source_data_encoded = "data12_encoded.txt"
    source_data_table = "data12_table.txt"

    # decoding output
    output_decoding = "hw12_05_201502085_decoded.txt"

    try:

        dic = dict()

        fr = open(source_data, 'r')

        pq = PriorityQueue()

        line = fr.readline()

        # make dict
        for i in range(0, len(line)):
            if line[i] in dic.keys():
                dic[line[i]] = dic[line[i]] + 1
            else:
                dic[line[i]] = 1

        # make pq
        for item in dic:
            pq.put(Node(item, dic[item], None, None))

        resDict = huffman_encode(pq, len(dic))
        resDict = sorted(resDict.items())

        with open(os.getcwd() + '/' + output_encoding_table, 'w', encoding='utf-8') as f1:
            for item in resDict:
                alphabet = item
                f1.write(item[0] + " : " + str(item[1]) + '\n')

    except FileNotFoundError:
        print("test File Not Found!")

