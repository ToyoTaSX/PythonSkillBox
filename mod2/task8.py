s, char = input().split()
for i in range(len(s)):
    if s[i] != char:
        print(i)
        break