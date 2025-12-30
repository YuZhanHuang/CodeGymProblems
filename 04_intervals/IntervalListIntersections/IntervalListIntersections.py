# Interval List Intersections

from typing import List


def intervals_intersection(interval_list_a, interval_list_b):
    i, j = 0, 0
    ans: List[List[int]] = []
    
    # 同時掃描兩個列表
    while i < len(interval_list_a) and j < len(interval_list_b):
        a_start, a_end = interval_list_a[i]
        b_start, b_end = interval_list_b[j]
        
        # 計算可能的重疊區間
        start = max(a_start, b_start)
        end   = min(a_end, b_end)
        if start <= end:
            ans.append([start, end])
        
        # 推動結束得較早的那個指標
        if a_end < b_end:
            i += 1
        else:
            j += 1
    
    return ans


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([[1, 3], [5, 9]], [[2, 4], [6, 8]], [[2, 3], [6, 8]]),
        ([[3, 8]], [[5, 10]], [[5, 8]]),
        ([[1, 5], [10, 15]], [[6, 9], [12, 18]], [[12, 15]]),
        ([[1, 3], [5, 7], [9, 12]], [[2, 4], [6, 8], [10, 11]], [[2, 3], [6, 7], [10, 11]]),
        ([], [[1, 5]], []),
        ([[1, 5]], [], []),
        ([[0, 2], [5, 10], [13, 23], [24, 25]], [[1, 5], [8, 12], [15, 24], [25, 26]], [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]),
    ]
    
    print("Testing Interval List Intersections:")
    all_passed = True
    for i, (list_a, list_b, expected) in enumerate(test_cases, 1):
        result = intervals_intersection(list_a, list_b)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status}")
        if result != expected:
            print(f"  Input A:  {list_a}")
            print(f"  Input B:  {list_b}")
            print(f"  Output:   {result}")
            print(f"  Expected: {expected}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

