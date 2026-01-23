import os

python_code = {
    "P6_1_FindMethod": """def find_pattern_find(text, pattern):
    return text.find(pattern)

text = "This is a sample text where we search for a pattern"
pattern = "search"

index = find_pattern_find(text, pattern)

if index != -1:
    print("Pattern found at index:", index)
else:
    print("Pattern not found")""",
    "P6_2_RegexSearch": """import re

def find_pattern_regex(text, pattern):
    return bool(re.search(pattern, text))

text = "This is a sample text where we search for a pattern"
pattern = "search"

if find_pattern_regex(text, pattern):
    print("Pattern found")
else:
    print("Pattern not found")""",
    "P6_3_BruteForce": """def brute_force_match(text, pattern):
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

print("Pattern found:", brute_force_match(text, pattern))""",
    "P6_4_NaiveFindAll": """def naive_pattern_matching(text, pattern):
    n = len(text)
    m = len(pattern)
    occurrences = []

    for i in range(n - m + 1):
        match = True
        for j in range(m):
            if text[i + j] != pattern[j]:
                match = False
                break
        if match:
            occurrences.append(i)

    return occurrences

text = "ABABCABABABCABAB"
pattern = "ABAB"

print("Occurrences found at indices:", naive_pattern_matching(text, pattern))""",
    "P6_5_CaseInsensitive": """def case_insensitive_match(text, pattern):
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
    print("Pattern not found")""",
    "P6_6_TimeComparison": """import timeit
import re

def find_general(text, pattern):
    return text.find(pattern) != -1

def find_regex(text, pattern):
    return bool(re.search(pattern, text))

def brute_force(text, pattern):
    n = len(text)
    m = len(pattern)
    for i in range(n - m + 1):
        if text[i:i+m] == pattern:
            return True
    return False

text = "This is a sample text where we search for a pattern"
pattern = "search"

t1 = timeit.timeit(lambda: find_general(text, pattern), number=10000)
t2 = timeit.timeit(lambda: find_regex(text, pattern), number=10000)
t3 = timeit.timeit(lambda: brute_force(text, pattern), number=10000)

print("Time using find():", t1)
print("Time using regex:", t2)
print("Time using brute force:", t3)""",
    "P6_7_TimeComplexity": """def naive_match(text, pattern):
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

print("Pattern found at index:", naive_match(text, pattern))"""
}

os.makedirs("python_practicals", exist_ok=True)
for name, code in python_code.items():
    with open(f"python_practicals/{name}.py", "w") as f:
        f.write(code)
print("Extracted 7 Python files.")
