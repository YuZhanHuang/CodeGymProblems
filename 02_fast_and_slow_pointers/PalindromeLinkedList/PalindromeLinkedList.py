from utils.data_structures import create_linked_list


def palindrome(head):
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    reversed_head = reverse_linked_list(slow)
    tmp_idx = head

    while reversed_head is not None:
        if reversed_head.data != tmp_idx.data:
            return False
        tmp_idx = tmp_idx.next
        reversed_head = reversed_head.next

    return True

def reverse_linked_list(ptr):
    prev = None
    next = None
    curr = ptr
    while curr is not None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev


def main():
    """Test cases for Palindrome Linked List"""
    test_cases = [
        # (values, expected_output, description)
        ([1, 2, 3, 2, 1], True, "Odd length palindrome"),
        ([1, 2, 2, 1], True, "Even length palindrome"),
        ([1, 2, 3, 4, 5], False, "Not a palindrome"),
        ([1], True, "Single node is palindrome"),
        ([1, 1], True, "Two same nodes is palindrome"),
    ]
    
    print("=" * 70)
    print("Testing: Palindrome Linked List")
    print("=" * 70)
    
    all_passed = True
    for i, (values, expected, description) in enumerate(test_cases, 1):
        head = create_linked_list(values)
        result = palindrome(head)
        passed = result == expected
        all_passed = all_passed and passed
        
        status = "✓ PASS" if passed else "✗ FAIL"
        print(f"\nTest {i}: {status}")
        print(f"  Input: {values}")
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

