def func(s):
    for i in range(10):
        if s.count(str(i)) > 1:
            return True
    return False

print(func(input()))

