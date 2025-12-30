# Longest Happy String

import heapq


def longest_diverse_string(a, b, c):
    # 1. 把正數次數存成負數，推入 max-heap（heapq 是 min-heap）
    heap = []
    for count, ch in [(a, 'a'), (b, 'b'), (c, 'c')]:
        if count > 0:
            heapq.heappush(heap, (-count, ch))

    res = []

    while heap:
        cnt1, ch1 = heapq.heappop(heap)
        rem1 = -cnt1  # 轉回正數，表示還剩多少可用
      
        # 如果會連續三個相同，就拿次多的出來
        if len(res) >= 2 and res[-1] == res[-2] == ch1:
            if not heap:
                break       # 沒有第二多，必須停
            cnt2, ch2 = heapq.heappop(heap)
            rem2 = -cnt2

            # 用掉一個 ch2
            rem2 -= 1       # 用減法表達「使用過一個」
            res.append(ch2)

            # ch2 還有剩再推回 heap（存成負數）
            if rem2 > 0:
                heapq.heappush(heap, (-rem2, ch2))
            # 把剛才被跳過的 ch1 推回 heap
            heapq.heappush(heap, (-rem1, ch1))

        else:
            # 直接用 ch1
            rem1 -= 1       # 用減法表示「使用過一個」
            res.append(ch1)
            # rem1 > 0 時再推回 heap
            if rem1 > 0:
                heapq.heappush(heap, (-rem1, ch1))

    return ''.join(res)


# Test cases
if __name__ == "__main__":
    test_cases = [
        (1, 1, 7, 8),  # Length should be close to 9
        (2, 2, 1, 5),
        (7, 1, 0, 8),
    ]
    
    print("Testing Longest Happy String:")
    all_passed = True
    for i, (a, b, c, expected_len) in enumerate(test_cases, 1):
        result = longest_diverse_string(a, b, c)
        
        # Validate the result
        valid = True
        # Check no three consecutive same characters
        for j in range(len(result) - 2):
            if result[j] == result[j+1] == result[j+2]:
                valid = False
                break
        
        # Check counts
        if result.count('a') > a or result.count('b') > b or result.count('c') > c:
            valid = False
        
        status = "✓" if valid else "✗"
        if not valid:
            all_passed = False
        print(f"Test {i}: {status} longest_diverse_string({a}, {b}, {c}) = '{result}' (len={len(result)})")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

