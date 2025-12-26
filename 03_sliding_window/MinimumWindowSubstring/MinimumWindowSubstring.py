# Minimum Window Substring


def min_window(s, t):
    if not s or not t:
        return ""

    req_dict = {}
    for i in t:
        req_dict[i] = 1 + req_dict.get(i, 0)

    cur_win = {}
    required, current = len(req_dict.keys()), 0
    res, res_len = [-1, -1], float("inf")

    left = 0
    for right in range(len(s)):
        if s[right] in req_dict:
            cur_win[s[right]] = cur_win.get(s[right], 0) + 1

            if cur_win[s[right]] == req_dict[s[right]]:
                current += 1

        while current == required:
            temp_len = right - left + 1
            if temp_len < res_len:
                res = [left, right]
                res_len = temp_len

            if s[left] in req_dict:
                cur_win[s[left]] -= 1
                if cur_win[s[left]] < req_dict[s[left]]:
                    current -= 1

            left += 1

    left, right = res
    return s[left : right + 1] if res_len != float("inf") else ""


# Driver code
def main():
    # Test case 1: Basic case
    s1 = "ADOBECODEBANC"
    t1 = "ABC"
    result1 = min_window(s1, t1)
    expected1 = "BANC"
    print(f"Test 1: {result1 == expected1} (Expected: {expected1}, Got: {result1})")

    # Test case 2: No valid window
    s2 = "a"
    t2 = "aa"
    result2 = min_window(s2, t2)
    expected2 = ""
    print(f"Test 2: {result2 == expected2} (Expected: {expected2}, Got: {result2})")

    # Test case 3: Entire string is minimum window
    s3 = "a"
    t3 = "a"
    result3 = min_window(s3, t3)
    expected3 = "a"
    print(f"Test 3: {result3 == expected3} (Expected: {expected3}, Got: {result3})")

    # Test case 4: Multiple valid windows
    s4 = "ABAACBAB"
    t4 = "ABC"
    result4 = min_window(s4, t4)
    expected4 = "ACB"  # Shortest window
    print(f"Test 4: {result4 == expected4} (Expected: {expected4}, Got: {result4})")

    # Test case 5: Duplicate characters in t
    s5 = "aaabbbbbcdd"
    t5 = "abcdd"
    result5 = min_window(s5, t5)
    expected5 = "abbbbbcdd"  # Need at least 1 'a', so can't skip the 'a's
    print(f"Test 5: {result5 == expected5} (Expected: {expected5}, Got: {result5})")


if __name__ == "__main__":
    main()
