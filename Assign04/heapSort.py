class Heap:
    def __init__(self, initial_capacity):
        self.count = 0
        self.capacity = initial_capacity
        self.arr = []

    def insert(self):
        pass

    def remove(self):
        pass

    def is_empty(self):
        return self.count == 0

    def length(self):
        return self.count

    def print(self):
        for i in range(0, self.count):
            print(self.arr[i])

    def max_heapify(self):
        pass


if __name__ == "__main__":
    pass

