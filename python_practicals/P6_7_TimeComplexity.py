def naive_match(text, pattern):
    n = len(text)
    m = len(pattern)
    for i in range(n - m + 1):
        for j in range(m):
            if text[i + j] != pattern[j]:
                break
        else:
            return i
    return -1

text = "A" * 1000 + "B"
pattern = "AB"

print("Pattern found at index:", naive_match(text, pattern))