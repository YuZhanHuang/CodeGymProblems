# Reverse Words in a String

import re


def reverse_words(sentence):
    trimmed_sentence = re.sub(' +',' ',sentence.strip())
    reversed_sentence = list(trimmed_sentence[::-1])
    start, end, n = 0, 0, len(reversed_sentence)
    
    while start < n:
        while end < n and reversed_sentence[end] != ' ':
            end += 1
            
        str_rev(reversed_sentence, start, end - 1)
        start = end + 1
        end = start
    
    return ''.join(reversed_sentence)


def str_rev(_str, start_rev, end_rev):
    while start_rev < end_rev:
        _str[start_rev], _str[end_rev] = _str[end_rev], _str[start_rev]
        start_rev += 1
        end_rev -= 1


# Test cases
if __name__ == "__main__":
    test_cases = [
        ("hello world", "world hello"),
        ("  hello world  ", "world hello"),
        ("a good   example", "example good a"),
        ("the sky is blue", "blue is sky the"),
        ("  Bob    Loves  Alice   ", "Alice Loves Bob"),
        ("Alice does not even like bob", "bob like even not does Alice"),
        ("hello", "hello"),
        ("  hello  ", "hello"),
    ]
    
    print("Testing Reverse Words in a String:")
    all_passed = True
    for i, (sentence, expected) in enumerate(test_cases, 1):
        result = reverse_words(sentence)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status}")
        print(f"  Input:    '{sentence}'")
        print(f"  Output:   '{result}'")
        print(f"  Expected: '{expected}'")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

