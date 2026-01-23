def brute_force_match(text, pattern):
    n = len(text)
    m = len(pattern)

    for i in range(n - m + 1):
        j = 0
        while j < m:
            if text[i + j] != pattern[j]:
                break
            j += 1
        if j == m:
            return True
    return False

text = "This is a sample text"
pattern = "sample"

print("Pattern found:", brute_force_match(text, pattern))