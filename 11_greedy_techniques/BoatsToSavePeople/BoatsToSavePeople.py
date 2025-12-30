# Boats to Save People

def rescue_boats(people, limit):
    left, right = 0, len(people) - 1
    count = 0
    people.sort()

    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1
            right -= 1
            count += 1
        else:
            count += 1
            right -= 1

    return count


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([1, 2], 3, 1),
        ([3, 2, 2, 1], 3, 3),
        ([3, 5, 3, 4], 5, 4),
    ]
    
    print("Testing Boats to Save People:")
    all_passed = True
    for i, (people, limit, expected) in enumerate(test_cases, 1):
        result = rescue_boats(people.copy(), limit)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status} rescue_boats({people}, {limit}) = {result}, expected {expected}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

