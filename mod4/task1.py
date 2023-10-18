lst = list(map(int, input().split()))
unique_count = len(set(lst))


if unique_count == len(lst):
    print("Все числа разные")
elif unique_count == 1:
    print("Все числа ранвы")
else:
    print("Есть равные и неравные числа")