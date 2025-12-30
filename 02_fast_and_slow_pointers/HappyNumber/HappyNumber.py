def sum_of_squared_digits(number):
    total_sum = 0
    while number > 0:
        digit = number % 10
        number = number // 10
        total_sum += digit ** 2
    return total_sum


def is_happy_number(n):
    slow, fast = n, n
    if n == 1:
        return True
      
    while True:
        slow = sum_of_squared_digits(slow)
        fast = sum_of_squared_digits(sum_of_squared_digits(fast))
        if fast == 1:
            return True
        if slow == fast:
            return False


def main():
    """Test cases for Happy Number"""
    test_cases = [
        # (input, expected_output, description)
        (19, True, "19 is a happy number (1^2 + 9^2 = 82, 8^2 + 2^2 = 68, ... -> 1)"),
        (1, True, "1 is a happy number by definition"),
        (2, False, "2 enters a cycle and never reaches 1"),
        (7, True, "7 is a happy number"),
        (20, False, "20 is not a happy number (enters cycle)"),
    ]
    
    print("=" * 70)
    print("Testing: Happy Number")
    print("=" * 70)
    
    all_passed = True
    for i, (n, expected, description) in enumerate(test_cases, 1):
        result = is_happy_number(n)
        passed = result == expected
        all_passed = all_passed and passed
        
        status = "✓ PASS" if passed else "✗ FAIL"
        print(f"\nTest {i}: {status}")
        print(f"  Input: {n}")
        print(f"  Expected: {expected}")
        print(f"  Got: {result}")
        print(f"  Description: {description}")
    
    print("\n" + "=" * 70)
    if all_passed:
        print("All tests PASSED! ✓")
    else:
        print("Some tests FAILED! ✗")
    print("=" * 70)
    
    return all_passed


if __name__ == "__main__":
    main()

