def power(base, n):
    if n == 0:
        return 1
    elif n == 1:
        return base
    elif n % 2 == 0:
        return power(base, n/2) * power(base, n/2)
    else:
        return power(base, (n-1)/2) * power(base, (n-1)/2) * base

if __name__ == "__main__":
    print(power(2, 30))

