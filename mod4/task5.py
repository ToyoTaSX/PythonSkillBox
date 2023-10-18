def get_counts(s: str) -> dict:
    result = dict()
    for ch in s:
        if ch.isalpha():
            if ch in result:
                result[ch] += 1
            else:
                result[ch] = 1
    return result

def get_file_statistics(filename: str) -> dict:
    s = ''
    with open(filename, 'r', encoding='utf-8') as file:
        s = ' '.join(file.readlines())
    return dict(sorted(get_counts(s).items(), key= lambda item: item[1]))

print(get_file_statistics("test.txt"))