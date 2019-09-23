def fibonacci_recursive(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def fibonacci_bottomup(n):
    if n == 0: return 0
    prev1 = 0
    prev2 = 1

    for i in range(2, n + 1, 1):
        temp = prev2
        prev2 = prev1 + prev2
        prev1 = temp

    return prev2

def fibonacci_squaring(n):
    if n < 2:
        return n

    matrix = [[1, 1], [1, 0]]

    POW.cache = dict()
    return POW(matrix, n)[1][0]

def POW(A, n):
    if n == 1:
        return A

    # Apply DP
    if n in POW.cache:
        return POW.cache[n]

    if n % 2 == 0:
        POW.cache[n] = MultiplyMatrix(POW(A, n/2), POW(A, n/2))
    else:
        POW.cache[n] = MultiplyMatrix(MultiplyMatrix(POW(A, (n-1)/2), POW(A, (n-1)/2)), A)

    return POW.cache[n]

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
