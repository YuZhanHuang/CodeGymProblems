# Minimum Number of Moves to Make Palindrome


def min_moves_to_make_palindrome(s: str) -> int:
    chars = list(s)
    n = len(chars)
    l, r = 0, n - 1
    moves = 0

    while l < r:
        # 如果本來就相等，就直接縮小範圍
        if chars[l] == chars[r]:
            l += 1
            r -= 1
            continue

        # 從右邊往左找，想找一個跟 chars[l] 一樣的字元
        k = r
        while k > l and chars[k] != chars[l]:
            k -= 1

        if k == l:
            # 情況 B：沒找到配對，chars[l] 是孤單字元，只能往中間推
            chars[l], chars[l + 1] = chars[l + 1], chars[l]
            moves += 1
        else:
            # 情況 A：在 k 找到配對，把 chars[k] 冒泡到 r
            while k < r:
                chars[k], chars[k + 1] = chars[k + 1], chars[k]
                k += 1
                moves += 1
            # 完成這一對的配對
            l += 1
            r -= 1

    return moves


# Test cases
if __name__ == "__main__":
    test_cases = [
        ("aabb", 2),
        ("letelt", 2),
        ("aa", 0),
        ("a", 0),
        ("abcba", 0),
        ("skoos", 1),
        ("ccxx", 2),
    ]

    print("Testing Minimum Number of Moves to Make Palindrome:")
    all_passed = True
    for i, (s, expected) in enumerate(test_cases, 1):
        result = min_moves_to_make_palindrome(s)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(
            f"Test {i}: {status} min_moves_to_make_palindrome('{s}') = {result}, expected {expected}"
        )

    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")
