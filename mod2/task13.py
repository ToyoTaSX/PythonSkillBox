code = input()
sum = (sum([int(code[i]) for i in range(0, len(code), 2)])
        + 3 * sum([int(code[i]) for i in range(1, len(code), 2)]))
print("yes" if sum % 90 == 0 else "no")
