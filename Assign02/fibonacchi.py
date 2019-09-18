def fibonacci_recursive(n):
    if n == 0:
        return 0;
    if n == 1:
        return 1;

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



if __name__ == "__main__":
    print(fibonacci_recursive(5))
    print(fibonacci_bottomup1(5))
    print(fibonacci_bottomup2(5))