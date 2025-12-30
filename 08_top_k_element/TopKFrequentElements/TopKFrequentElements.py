# Top K Frequent Elements

from heapq import heappush, heappop


def top_k_frequent(arr, k):
    freq = {}
    min_heap = []
    for ele in arr:
        freq[ele] = 1 + freq.get(ele, 0)
    
    freq_list = [(val, key) for key, val in freq.items()]
    
    if k >= len(freq_list):
        return [key for key, val in freq.items()]
    
    for i in range(k):
        val, key = freq_list[i]
        heappush(min_heap, (val, key))

    for j in range(k, len(freq_list)):
        val, key = freq_list[j]
        if min_heap[0][0] < val:
            heappop(min_heap)
            heappush(min_heap, (val, key))
    
    return [key for (val, key) in min_heap]


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([1, 1, 1, 2, 2, 3], 2, [1, 2]),
        ([1], 1, [1]),
        ([1, 2], 2, [1, 2]),
    ]
    
    print("Testing Top K Frequent Elements:")
    all_passed = True
    for i, (arr, k, expected) in enumerate(test_cases, 1):
        result = top_k_frequent(arr, k)
        # Sort both for comparison
        result_sorted = sorted(result)
        expected_sorted = sorted(expected)
        status = "✓" if result_sorted == expected_sorted else "✗"
        if result_sorted != expected_sorted:
            all_passed = False
        print(f"Test {i}: {status} top_k_frequent({arr}, {k}) = {result}, expected {expected}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

