# Search in Rotated Sorted Array II

def search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return True

        if arr[left] < arr[mid] or arr[mid] > arr[right]:
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        elif arr[mid] < arr[right] or arr[mid] < arr[left]:
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
        else:
            left += 1

    return False


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([2, 5, 6, 0, 0, 1, 2], 0, True),
        ([2, 5, 6, 0, 0, 1, 2], 3, False),
        ([1, 0, 1, 1, 1], 0, True),
    ]
    
    print("Testing Search in Rotated Sorted Array II:")
    all_passed = True
    for i, (arr, target, expected) in enumerate(test_cases, 1):
        result = search(arr, target)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status} search({arr}, {target}) = {result}, expected {expected}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

