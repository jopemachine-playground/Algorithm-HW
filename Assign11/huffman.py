class Node:
    def __init__ (self, alphabet, freq):

        self.freq = freq
        self.left = None
        self.right = None
        self.alphabet = alphabet


def huffman_encode(C):
    n = len(C)

    for i in range(1, n):
        z = Node()


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
