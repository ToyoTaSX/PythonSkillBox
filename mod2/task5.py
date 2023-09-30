char, delta = input().split(',')
delta = int(delta)
print(chr(97 + ((ord(char) - 97) + delta)% 26))