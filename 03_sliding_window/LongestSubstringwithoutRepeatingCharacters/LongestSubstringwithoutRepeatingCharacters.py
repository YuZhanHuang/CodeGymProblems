def find_longest_substring(input_str):
    if not input_str:
        return 0

    seen = {}  # 記錄每個字元上次出現的位置
    start = 0  # 當前無重複子字串的起始索引
    max_len = 0
    end = 0

    while end < len(input_str):
        c = input_str[end]
        # 只有當字元上次出現位置還在目前視窗 [start, end) 內，才認定為重複
        if c in seen and seen[c] >= start:
            start = seen[c] + 1

        # 更新這個字元最新出現的位置
        seen[c] = end

        # 計算並更新最長長度
        curr_len = end - start + 1
        if curr_len > max_len:
            max_len = curr_len

        end += 1

    return max_len


# Driver code
def main():
    # Test case 1: Basic case with repeating characters
    s1 = "abcabcbb"
    result1 = find_longest_substring(s1)
    expected1 = 3  # "abc"
    print(f"Test 1: {result1 == expected1} (Expected: {expected1}, Got: {result1})")

    # Test case 2: All same characters
    s2 = "bbbbb"
    result2 = find_longest_substring(s2)
    expected2 = 1  # "b"
    print(f"Test 2: {result2 == expected2} (Expected: {expected2}, Got: {result2})")

    # Test case 3: No repeating characters
    s3 = "pwwkew"
    result3 = find_longest_substring(s3)
    expected3 = 3  # "wke"
    print(f"Test 3: {result3 == expected3} (Expected: {expected3}, Got: {result3})")

    # Test case 4: Empty string
    s4 = ""
    result4 = find_longest_substring(s4)
    expected4 = 0  # Empty
    print(f"Test 4: {result4 == expected4} (Expected: {expected4}, Got: {result4})")

    # Test case 5: Single character
    s5 = "x"
    result5 = find_longest_substring(s5)
    expected5 = 1  # "x"
    print(f"Test 5: {result5 == expected5} (Expected: {expected5}, Got: {result5})")


if __name__ == "__main__":
    main()
