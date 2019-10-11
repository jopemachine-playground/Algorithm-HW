class PriorityQueue:
    # ----------------------------------------------------------------------------------------------------------------
    # Public Method
    class Node:
        # Node는 PQ의 노드 중첩 클래스
        def __init__(self, priority, item):
            self.priority = priority;
            self.item = item

    def dequeue(self):
        # extract_max (S)
        target = self.__arr[0]
        self.delete(target.item)
        return target

    def delete(self, item):
        for i in range(0, self.__count):
            if self.__arr[i].item == item:
                temp = self.__arr
                for j in range(i, self.__count - 1):
                    self.__arr[j] = temp[j + 1]

        self.__count -= 1
        self.__arr.pop()

        for i in range(int(len(self.__arr) / 2), 0, -1):
            # max_heapify는 root 노드 인덱스를 1이라고 가정하지만,
            # 배열의 시작 인덱스는 0임. 따라서, 1을 빼 준다.
            self.__max_heapify(i-1)
        return

    def enqueue(self, item, priority):
        # insert (S, x)
        self.__arr.append(self.Node(int(priority), item))
        self.__count += 1

        for i in range(int(self.__count / 2), 0, -1):
            # max_heapify는 root 노드 인덱스를 1이라고 가정하지만,
            # 배열의 시작 인덱스는 0임. 따라서, 1을 빼 준다.
            self.__max_heapify(i-1)

    def increase_priority(self, item, priority):
        # increase_key(S, x, k)
        for i in range(0, self.__count):
            if self.__arr[i].item == item:
                self.__arr[i].priority = int(priority)
                break

        for i in range(int(self.__count / 2), 0, -1):
            # max_heapify는 root 노드 인덱스를 1이라고 가정하지만,
            # 배열의 시작 인덱스는 0임. 따라서, 1을 빼 준다.
            self.__max_heapify(i-1)

    def is_empty(self):
        return self.count == 0

    def length(self):
        return self.count

    def print(self):
        for i in range(0, self.__count):
            print(str(self.__arr[i].priority) + ", " + self.__arr[i].item)

    def retrieve(self):
        # max (S)
        return self.__arr[0].item

    # ----------------------------------------------------------------------------------------------------------------

    # Private Method

    def __init__(self):
        self.__count = 0
        self.__arr = []

    def __init__(self, arr):
        # Build_Max_Heap
        self.__count = len(arr)
        self.__arr = arr
        for i in range(int(len(arr) / 2), 0, -1):
            # max_heapify는 root 노드 인덱스를 1이라고 가정하지만,
            # 배열의 시작 인덱스는 0임. 따라서, 1을 빼 준다.
            self.__max_heapify(i-1)

    def __max_heapify(self, index):
        left_child_index = index * 2 + 1
        right_child_index = index * 2 + 2

        if left_child_index < self.__count and self.__arr[left_child_index].priority > self.__arr[index].priority:
            largest = left_child_index
        else:
            largest = index

        if right_child_index < self.__count and self.__arr[right_child_index].priority > self.__arr[largest].priority:
            largest = right_child_index

        if largest != index:
            self.__arr[index], self.__arr[largest] = self.__arr[largest],  self.__arr[index]
            self.__max_heapify(largest)

    @staticmethod
    def __get_parent_index(child_index):
        if child_index:
            return 0

        if child_index % 2 == 0:
            return (child_index / 2) - 1
        else:
            return child_index / 2


# ----------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    source_data = "data04.txt"
    records = []

    try:
        fr = open(source_data, 'r')
        while True:
            line = fr.readline()
            if not line:
                break
            score = int(line.split(",")[0].strip())
            text = line.split(",")[1].strip()
            records.append(PriorityQueue.Node(score, text))

    except FileNotFoundError:
        print("test File Not Found!")

    pq = PriorityQueue(records)

    while True:
        print("**** 현재 우선 순위 큐에 저장되어 있는 작업 대기 목록은 다음과 같습니다. ****")
        print()

        pq.print()
        print()
        print("-" * 75)

        print("1. 작업 추가  2. 최대값  3. 최대 우선순위 작업 처리")
        print("4. 원소 키값 증가  5. 작업 제거  6. 종료")
        print("-" * 75)

        command = input()

        if command == "1":
            print("추가할 작업의 우선순위를 입력해주세요")
            prio = input()
            print("추가할 작업의 이름을 입력해주세요")
            work = input()
            pq.enqueue(work, prio)
            print("-" * 75)

        elif command == "2":
            print("가장 높은 우선순위를 갖는 항목은 " + pq.retrieve() + " 입니다")
            print("-" * 75)

        elif command == "3":
            task = pq.dequeue()
            print("가장 높은 우선순위의 작업을 처리했습니다. 처리된 작업은 " + task.item + " 입니다")
            print("-" * 75)

        elif command == "4":
            print("증가시킬 항목의 이름을 입력해주세요")
            work = input()
            print("증가시킬 키 값을 입력해주세요 (감소는 불가)")
            prio = input()
            pq.increase_priority(work, prio)
            print("-" * 75)

        elif command == "5":
            print("제거할 항목의 이름을 입력하세요")
            work = input()
            pq.delete(work)
            print("-" * 75)

        elif command == "6":
            print("프로그램을 종료합니다")
            break




