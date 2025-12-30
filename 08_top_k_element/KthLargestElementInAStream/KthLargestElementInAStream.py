# Kth Largest Element in a Stream

import heapq


class KthLargest:
    # Constructor to initialize heap and add values in it
    def __init__(self, k, nums):
        self.k = k
        self.heap = []
        for num in nums:
            self.add(num)

    # Adds element in the heap and return the Kth largest
    def add(self, val):
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heappop(self.heap)
            heapq.heappush(self.heap, val)
        
        return self.heap[0]


# Test cases
if __name__ == "__main__":
    test_cases = [
        (3, [4, 5, 8, 2], [3, 5, 10, 9, 4], [4, 5, 5, 8, 8]),
        (1, [], [3, 1, 5, 12, 2, 11], [3, 3, 5, 12, 12, 12]),
    ]
    
    print("Testing Kth Largest Element in a Stream:")
    all_passed = True
    for i, (k, nums, add_values, expected) in enumerate(test_cases, 1):
        kth_largest = KthLargest(k, nums)
        result = []
        for val in add_values:
            result.append(kth_largest.add(val))
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status} KthLargest({k}, {nums}), add({add_values}) = {result}, expected {expected}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

