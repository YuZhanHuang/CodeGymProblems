# Next Palindrome Using Same Digits

from typing import List


def next_permutation(chars: List[str]) -> bool:
    """
    對 chars 進行 in-place 的「下一個排列（字典序）」。
    若成功找到下一個排列，回傳 True；若已是最大排列，回傳 False。

    演算法步驟（標準 next_permutation）：
    1. 從右往左找第一個 i，使得 chars[i] < chars[i+1] （稱為 pivot）。
       若找不到，代表整個序列是非遞增（例如 3 2 2 1），沒有下一個排列，回傳 False。

    2. 再從右往左找第一個 j，使得 chars[j] > chars[i]。
       這個 j 是在 suffix 中，距離右側最近、且比 pivot 大的元素。

    3. 交換 chars[i], chars[j]。

    4. 將 i 之後的 suffix 反轉，使其變成最小的遞增序列。
    """
    n = len(chars)
    if n <= 1:
        return False

    # 1. 找 pivot：從右往左找第一個 chars[i] < chars[i+1]
    i = n - 2
    while i >= 0 and chars[i] >= chars[i + 1]:
        i -= 1

    if i < 0:
        # 已經是最大的排列
        return False

    # 2. 從右往左找第一個比 chars[i] 大的元素 j
    j = n - 1
    while j > i and chars[j] <= chars[i]:
        j -= 1

    # 3. 交換 pivot 與 j
    chars[i], chars[j] = chars[j], chars[i]

    # 4. 將 i 之後的 suffix 反轉
    left, right = i + 1, n - 1
    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1

    return True


def next_palindrome_same_digits(num_str: str) -> str:
    """
    給定一個回文字串 num_str（只包含數字），回傳
    「用同樣 digits 可以組成的下一個較大的回文」。
    若不存在，回傳空字串 ""。
    """
    n = len(num_str)
    if n <= 1:
        # 單一字元本身就是唯一回文，沒有更大
        return ""

    # 對於奇數長度，需要對「左半邊+中間字符」一起做 next permutation
    # 對於偶數長度，只對左半邊做 next permutation
    if n % 2 == 1:
        # 奇數長度：左半邊包含中間字符
        half_with_mid = list(num_str[: n // 2 + 1])
        if not next_permutation(half_with_mid):
            return ""
        # 新回文：前半部分 + 反轉（不含中間）
        new_str = "".join(half_with_mid) + "".join(half_with_mid[-2::-1])
        return new_str
    else:
        # 偶數長度
        half = list(num_str[: n // 2])
        if not next_permutation(half):
            return ""
        # 組出新的回文：half + reverse(half)
        new_left = "".join(half)
        new_right = new_left[::-1]
        return new_left + new_right


# Test cases
if __name__ == "__main__":
    test_cases = [
        ("123321", "132231"),
        ("1221", "2112"),
        ("11", ""),
        ("9", ""),
        ("12321", "13231"),
        ("99", ""),
        ("1234321", "1243421"),
        ("54345", ""),  # 543 is max permutation, no next palindrome
    ]
    
    print("Testing Next Palindrome Using Same Digits:")
    all_passed = True
    for i, (num_str, expected) in enumerate(test_cases, 1):
        result = next_palindrome_same_digits(num_str)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status} next_palindrome_same_digits('{num_str}') = '{result}', expected '{expected}'")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

