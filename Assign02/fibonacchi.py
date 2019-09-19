def fibonacci_recursive(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def fibonacci_bottomup1(n):
    cache = [None] * (n+1)
    cache[0] = 0
    cache[1] = 1
    for i in range(2, n + 1, 1):
        cache[i] = cache[i-1] + cache[i-2]
    return cache[n]

def fibonacci_bottomup2(n):
    prev1 = 0
    prev2 = 1
    for i in range(2, n + 1, 1):
        temp = prev2
        prev2 = prev1 + prev2
        prev1 = temp

    return prev2

def fibonacci_squaring(n):
    matrix = [[0]*2 for i in range(2)]
    matrix = {{1, 1}, {1, 0}}
    ret = [[0]*2 for i in range(2)]
    ret = {{1, 1}, {1, 0}}
    for i in range(0, n, 1):
        ret = MultiplyMatrix(ret, matrix)


# assume Matrix A and B are same size
def MultiplyMatrix(Matrix_A, Matrix_B):
    ret = [[None]*len(Matrix_A) for i in range(0, len(Matrix_A))]
    for i in range(0, len(Matrix_A)):
        for j in range(0, len(Matrix_A)):
            for k in range(0, len(Matrix_A)):
                ret[i][j] = Matrix_A[i][j] * Matrix_B[j][k]
    return ret;


if __name__ == "__main__":
    print(fibonacci_recursive(5))
    print(fibonacci_bottomup1(5))
    print(fibonacci_bottomup2(5))
    print(fibonacci_squaring(5))