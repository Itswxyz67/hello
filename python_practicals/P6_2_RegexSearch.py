import re

def find_pattern_regex(text, pattern):
    return bool(re.search(pattern, text))

text = "This is a sample text where we search for a pattern"
pattern = "search"

if find_pattern_regex(text, pattern):
    print("Pattern found")
else:
    print("Pattern not found")