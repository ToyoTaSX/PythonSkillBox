chars = 'аеиоёю'
s = input()
c = 0
for i in s:
    if i in chars:
        c += 1
print(c, len(s.replace(" ", "")) - c)
