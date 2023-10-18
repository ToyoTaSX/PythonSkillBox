def fast_pow(a, n):
    if n == 0:
        return 1
    elif n == 1:
        return a

    if n % 2 == 0:
        return fast_pow(a * a, n // 2)
    else:
        return a * fast_pow(a, n - 1)

a, n = map(int, input().split())
print(fast_pow(a, n))