import timeit

def fibonacci_recursive(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# def fibonacci_bottomup1(n):
#     cache = [None] * (n+1)
#
#     print("-------------------------------------------------------")
#     cache[0] = 0
#     cache[1] = 1
#     print("f< 0>" + cache[0])
#     print("f< 1>" + cache[1])
#
#     for i in range(2, n + 1, 1):
#         if i % 10 == 0:
#             print("-------------------------------------------------------")
#         cache[i] = cache[i-1] + cache[i-2]
#         print("f< " + str(i) + ">" + cache[i])
#     return cache[n]

def fibonacci_bottomup2(n):

    print('-' * 80)
    prev1 = 0
    prev2 = 1

    for i in range(2, n + 1, 1):
        temp = prev2
        prev2 = prev1 + prev2
        prev1 = temp

    return prev2

def fibonacci_squaring(n):
    matrix = [[1, 1], [1, 0]]
    ret = matrix
    start = timeit.default_timer()

    print('-' * 80)
    for i in range(1, n):
        ret = MultiplyMatrix(ret, matrix)
    return ret[1][0]


# assume Matrix A and B are same size
def MultiplyMatrix(Matrix_A, Matrix_B):
    ret = [[None]*len(Matrix_A) for i in range(0, len(Matrix_A))]
    for i in range(0, len(Matrix_A)):
        for j in range(0, len(Matrix_A)):
            sum = 0
            for k in range(0, len(Matrix_A)):
                sum += Matrix_A[i][k] * Matrix_B[k][j]
            ret[i][j] = sum
    return ret;


if __name__ == "__main__":
    pass
    # print(fibonacci_recursive(5))
    # print(fibonacci_bottomup1(5))
    # print(fibonacci_bottomup2(90))
    # print(fibonacci_squaring(90))
    # print(MultiplyMatrix([[1, 1], [1, 0]], [[1, 1], [1, 0]]))
