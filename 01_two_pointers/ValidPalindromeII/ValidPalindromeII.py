# Valid Palindrome II

def valid_palindrome(s: str) -> bool:
    """
    判斷字串 s 是否能在最多移除一個字符後，成為回文串。
    回傳 True/False。
    """
    def is_pal(l: int, r: int) -> bool:
        """檢查 s[l..r] 區間是否為回文。"""
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    left, right = 0, len(s) - 1
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            # 嘗試跳過左邊或右邊的字符，只要任一成立即可
            return is_pal(left + 1, right) or is_pal(left, right - 1)
    return True


# Test cases
if __name__ == "__main__":
    test_cases = [
        ("aba", True),
        ("abca", True),  # remove 'c' or 'b'
        ("abc", False),
        ("racecar", True),
        ("raceacar", True),  # remove 'a' in middle
        ("abcdefghijklmnopqrstuvwxyz", False),
        ("a", True),
        ("ab", True),
        ("abcdcba", True),
        ("abcddcba", True),
        ("abcdedcba", True),
        ("aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga", True),
    ]
    
    print("Testing Valid Palindrome II:")
    all_passed = True
    for i, (s, expected) in enumerate(test_cases, 1):
        result = valid_palindrome(s)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status} valid_palindrome('{s[:20]}...') = {result}, expected {expected}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

