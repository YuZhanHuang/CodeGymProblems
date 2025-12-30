# Nested List Weight Sum II


def max_depth(nested_list):
    """
    Calculate the maximum depth of nested_list,
    where the outermost list has depth 1.
    """
    def dfs(lst, depth):
        max_d = depth
        for x in lst:
            if isinstance(x, list):
                max_d = max(max_d, dfs(x, depth + 1))
        return max_d

    return dfs(nested_list, 1)


def inverse_depth_sum(nested_list):
    """
    Calculate the inverse depth weighted sum of nested list:
      weight = max_depth - depth + 1
    Return the sum of all integers value * weight.
    """
    D = max_depth(nested_list)

    def dfs_sum(lst, depth):
        total = 0
        for x in lst:
            if isinstance(x, list):
                # Sub-list, depth +1
                total += dfs_sum(x, depth + 1)
            else:
                # Integer: calculate weight and accumulate
                w = D - depth + 1
                total += x * w
        return total

    return dfs_sum(nested_list, 1)


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([[1, 1], 2, [1, [2, [1]]]], 4, 22),  # (max_depth, expected_sum)
        ([[[[[[1]]]]]], 6, 1),
        ([1, 2, [3, [4, 3], 5]], 3, 32),
    ]
    
    print("Testing Nested List Weight Sum II:")
    all_passed = True
    for i, (nested_list, expected_depth, expected_sum) in enumerate(test_cases, 1):
        depth = max_depth(nested_list)
        result = inverse_depth_sum(nested_list)
        depth_ok = depth == expected_depth
        sum_ok = result == expected_sum
        status = "✓" if depth_ok and sum_ok else "✗"
        if not (depth_ok and sum_ok):
            all_passed = False
        print(f"Test {i}: {status} max_depth={depth} (expected {expected_depth}), sum={result} (expected {expected_sum})")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

