# Two City Scheduling

def two_city_scheduling(costs):
    costs.sort(key=lambda x: x[0] - x[1])
    left, right = 0, len(costs) - 1
    total = 0

    while left < right:
        total += (costs[left][0] + costs[right][1])
        left += 1
        right -= 1 

    return total


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([[10, 20], [30, 200], [400, 50], [30, 20]], 110),
        ([[259, 770], [448, 54], [926, 667], [184, 139], [840, 118], [577, 469]], 1859),
    ]
    
    print("Testing Two City Scheduling:")
    all_passed = True
    for i, (costs, expected) in enumerate(test_cases, 1):
        result = two_city_scheduling(costs)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status} two_city_scheduling(costs) = {result}, expected {expected}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

