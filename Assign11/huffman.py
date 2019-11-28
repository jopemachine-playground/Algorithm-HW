class Node:
    def __init__ (self, alphabet, freq):

        self.freq = freq;
        self.left = None;
        self.right = None;
        self.alphabet = alphabet;


def huffman(C):
    n = len(C)

    for i in range(1, n):
        z = Node()
