from utils.data_structures import create_linked_list


def get_middle_node(head):
    slow, fast = head, head

    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next

    return slow


def main():
    """Test cases for Middle of the Linked List"""
    test_cases = [
        # (values, expected_middle_value, description)
        ([1, 2, 3, 4, 5], 3, "Odd length list, middle is 3"),
        ([1, 2, 3, 4, 5, 6], 4, "Even length list, return second middle (4)"),
        ([1], 1, "Single node"),
        ([1, 2], 2, "Two nodes, return second"),
        ([1, 2, 3], 2, "Three nodes, return middle"),
    ]
    
    print("=" * 70)
    print("Testing: Middle of the Linked List")
    print("=" * 70)
    
    all_passed = True
    for i, (values, expected, description) in enumerate(test_cases, 1):
        head = create_linked_list(values)
        result_node = get_middle_node(head)
        result = result_node.val if result_node else None
        passed = result == expected
        all_passed = all_passed and passed
        
        status = "✓ PASS" if passed else "✗ FAIL"
        print(f"\nTest {i}: {status}")
        print(f"  Input: {values}")
        print(f"  Expected middle value: {expected}")
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

