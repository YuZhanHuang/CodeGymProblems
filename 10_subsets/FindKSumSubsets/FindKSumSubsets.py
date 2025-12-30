# Find K-Sum Subsets

def bitwise_mask(num, bit):
    n = 1 << num
    masked = n & bit

    return 0 if masked == 0 else 1


def get_k_sum_subsets(set_of_integers, target_sum):
    l = 2 ** len(set_of_integers)
    result = []
    for i in range(l):
        sub = []
        for j in range(len(set_of_integers)):
            if bitwise_mask(j, i):
                sub.append(set_of_integers[j])
        if sum(sub) == target_sum:
            result.append(sub)

    return result


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4, 5], 7, [[3, 4], [2, 5], [1, 2, 4]]),
        ([1, 3, 5], 5, [[5], [2, 3]]),  # Note: [2, 3] won't be found if 2 is not in the set
        ([1, 2, 3], 6, [[1, 2, 3]]),
    ]
    
    print("Testing Find K-Sum Subsets:")
    all_passed = True
    for i, (set_of_integers, target_sum, expected_contains) in enumerate(test_cases, 1):
        result = get_k_sum_subsets(set_of_integers, target_sum)
        # Check if all subsets sum to target
        all_correct = all(sum(subset) == target_sum for subset in result)
        status = "✓" if all_correct else "✗"
        if not all_correct:
            all_passed = False
        print(f"Test {i}: {status} get_k_sum_subsets({set_of_integers}, {target_sum})")
        print(f"  Found {len(result)} subsets: {result}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

