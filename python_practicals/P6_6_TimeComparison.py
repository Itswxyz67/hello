import timeit
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
print("Time using brute force:", t3)