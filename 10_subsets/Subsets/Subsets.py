# Subsets

def get_bit(num, bit):
    mask = 1 << bit  # 000 -> 001 表達取第一個元素
    masked = mask & num

    return 0 if masked == 0 else 1


def find_all_subsets(nums):
    if not nums:
        return [[]]

    result = []
    for i in range(0, 2 ** len(nums)):
        subset = set()
        for j in range(0, len(nums)):
            if get_bit(i, j) == 1 and nums[j] not in subset:
                subset.add(nums[j])

        if i == 0:
            result.append([])
        else:
            result.append(list(subset))

    return result


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3], 8),  # Should have 2^3 = 8 subsets
        ([0], 2),  # Should have 2^1 = 2 subsets
    ]
    
    print("Testing Subsets:")
    all_passed = True
    for i, (nums, expected_count) in enumerate(test_cases, 1):
        result = find_all_subsets(nums)
        status = "✓" if len(result) == expected_count else "✗"
        if len(result) != expected_count:
            all_passed = False
        print(f"Test {i}: {status} find_all_subsets({nums}) has {len(result)} subsets, expected {expected_count}")
        print(f"  Subsets: {result}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

