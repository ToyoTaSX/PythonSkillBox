def NOD(a, b):
    if a == 0 or b == 0:
        return a + b

    if a > b:
        return NOD(a - b, b)
    return NOD(a, b - a)

a, b = map(int, input().split())
print(NOD(a, b))