# Valid Palindrome

def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1 
        right -= 1
      
    return True


# Test cases
if __name__ == "__main__":
    test_cases = [
        ("racecar", True),
        ("hello", False),
        ("a", True),
        ("ab", False),
        ("aa", True),
        ("abba", True),
        ("abcba", True),
        ("abccba", True),
        ("abcdcba", True),
        ("", True),
    ]
    
    print("Testing Valid Palindrome:")
    all_passed = True
    for i, (s, expected) in enumerate(test_cases, 1):
        result = is_palindrome(s)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status} is_palindrome('{s}') = {result}, expected {expected}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")
