# Sliding Window Median

import heapq
from collections import defaultdict


def median_sliding_window(nums, k):
    small, large = [], []            # small 為 max-heap（存負值），large 為 min-heap
    delayed = defaultdict(int)       # 懶刪除計數器
    small_size = large_size = 0      # 記錄兩堆的「有效」元素數量
    
    
    def prune(heap):
        """
        清理 heap 頂端那些被標記為刪除的元素
        """
        while heap:
            num = -heap[0] if heap is small else heap[0]
            if delayed[num] > 0:
                delayed[num] -= 1
                heapq.heappop(heap)
            else:
                break

    def balance():
        """
        平衡兩堆大小，使 small_size == large_size or small_size == large_size + 1
        """
        nonlocal small_size, large_size
        # small 太大 → 拿一個到 large
        if small_size > large_size + 1:
            val = -heapq.heappop(small)
            small_size -= 1
            heapq.heappush(large, val)
            large_size += 1
            prune(small)
        # large 太大 → 拿一個到 small
        elif small_size < large_size:
            val = heapq.heappop(large)
            large_size -= 1
            heapq.heappush(small, -val)
            small_size += 1
            prune(large)

    def insert(num):
        """
        插入新數字到合適的堆，並呼叫 balance()
        """
        nonlocal small_size, large_size
        if not small or num <= -small[0]:
            heapq.heappush(small, -num)
            small_size += 1
        else:
            heapq.heappush(large, num)
            large_size += 1
        balance()

    def erase(num):
        """
        標記刪除 num，並在必要時清理堆頂，再呼叫 balance()
        """
        nonlocal small_size, large_size
        delayed[num] += 1
        # 調整 size 計數
        # 以下會先決定 num 是在 large 還是 small
        if num <= -small[0]:
            small_size -= 1
            if num == -small[0]:
                prune(small)
        else:
            large_size -= 1
            if large and num == large[0]:
                prune(large)
        balance()

    def get_median():
        """
        直接從兩堆堆頂計算中位數
        """
        if k & 1:
            return float(-small[0])
        return (-small[0] + large[0]) / 2.0

    res = []
    for i, num in enumerate(nums):
        insert(num)
        # 當窗口超過 k，刪除最左側數字
        if i >= k:
            erase(nums[i - k])
        # 從第 k-1 步開始，每次都記錄中位數
        if i >= k - 1:
            res.append(get_median())
    return res


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([1, 3, -1, -3, 5, 3, 6, 7], 3, [1.0, -1.0, -1.0, 3.0, 5.0, 6.0]),
        ([1, 2, 3, 4, 2, 3, 1, 4, 2], 3, [2.0, 3.0, 3.0, 3.0, 2.0, 3.0, 2.0]),
    ]
    
    print("Testing Sliding Window Median:")
    all_passed = True
    for i, (nums, k, expected) in enumerate(test_cases, 1):
        result = median_sliding_window(nums, k)
        # Check if results are close enough (within 10^-5)
        status = "✓" if all(abs(r - e) < 1e-5 for r, e in zip(result, expected)) else "✗"
        if not all(abs(r - e) < 1e-5 for r, e in zip(result, expected)):
            all_passed = False
        print(f"Test {i}: {status}")
        if not all(abs(r - e) < 1e-5 for r, e in zip(result, expected)):
            print(f"  Input: nums={nums}, k={k}")
            print(f"  Output:   {result}")
            print(f"  Expected: {expected}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

