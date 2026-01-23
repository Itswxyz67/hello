def case_insensitive_match(text, pattern):
    text = text.lower()
    pattern = pattern.lower()

    n = len(text)
    m = len(pattern)

    for i in range(n - m + 1):
        if text[i:i+m] == pattern:
            return i
    return -1

text = "Data Structures and Algorithms"
pattern = "algorithms"

index = case_insensitive_match(text, pattern)

if index != -1:
    print("Pattern found at index:", index)
else:
    print("Pattern not found")