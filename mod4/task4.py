def get_polyndrome(s):
    counts = get_counts(s)
    counts_odd = sum(item[1] % 2 != 0 for item in counts.items())
    if (counts_odd == 1 and len(s) % 2 == 0) or (counts_odd > 1):
        return

    result = ""
    odd_str = ''
    for key, value in counts.items():
        if value % 2 != 0:
            odd_str = key * value
            continue

        result += key * (value // 2)

    return result + odd_str + result[::-1]


def get_counts(s: str) -> dict:
    result = dict()
    for ch in s:
        if ch != ' ':
            result[ch] = s.count(ch)
    return result


print(get_polyndrome(input()))