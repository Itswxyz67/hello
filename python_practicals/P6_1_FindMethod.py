def find_pattern_find(text, pattern):
    return text.find(pattern)

text = "This is a sample text where we search for a pattern"
pattern = "search"

index = find_pattern_find(text, pattern)

if index != -1:
    print("Pattern found at index:", index)
else:
    print("Pattern not found")