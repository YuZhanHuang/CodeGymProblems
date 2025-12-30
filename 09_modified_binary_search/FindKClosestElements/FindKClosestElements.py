# Find K Closest Elements

def find_k_closest(nums, target, k):
    n = len(nums)
    low, high = 0, n - k

    # Binary‐search the best starting index
    while low < high:
        mid = (low + high) // 2
        # Compare distances at the two window ends
        if target - nums[mid] > nums[mid + k] - target:
            # Right‐end is closer ⇒ shift window right
            low = mid + 1
        else:
            # Left‐end is as close or closer ⇒ keep/shift window left
            high = mid

    # low == best starting index
    return nums[low : low + k]


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4, 5], 3, 4, [1, 2, 3, 4]),
        ([1, 2, 3, 4, 5], -1, 4, [1, 2, 3, 4]),
        ([1, 1, 1, 10, 10, 10], 9, 1, [10]),
    ]
    
    print("Testing Find K Closest Elements:")
    all_passed = True
    for i, (nums, target, k, expected) in enumerate(test_cases, 1):
        result = find_k_closest(nums, target, k)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status} find_k_closest({nums}, target={target}, k={k}) = {result}, expected {expected}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

