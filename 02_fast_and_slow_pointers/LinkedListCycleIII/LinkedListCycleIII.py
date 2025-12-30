from utils.data_structures import create_linked_list_with_cycle


def count_cycle_length(head):
    if not head:
        return 0

    
    slow, fast = head, head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return 0
    
    meet = slow
    count = 1
    curr = slow.next
    while curr != meet:  # Fixed: was "meet is not meet" which is always False
        count += 1
        curr = curr.next
        
    return count


def main():
    """Test cases for Linked List Cycle III (Length of Cycle)"""
    test_cases = [
        # (values, cycle_pos, expected_cycle_length, description)
        ([3, 2, 0, -4], 1, 3, "Cycle length is 3 (nodes: 2->0->-4)"),
        ([1, 2], 0, 2, "Cycle length is 2 (entire list)"),
        ([1], -1, 0, "No cycle, return 0"),
        ([1, 2, 3, 4, 5], -1, 0, "No cycle in list"),
        ([1, 2, 3, 4, 5, 6], 2, 4, "Cycle length is 4 (nodes: 3->4->5->6)"),
    ]
    
    print("=" * 70)
    print("Testing: Linked List Cycle III (Length of Cycle)")
    print("=" * 70)
    
    all_passed = True
    for i, (values, pos, expected, description) in enumerate(test_cases, 1):
        head = create_linked_list_with_cycle(values, pos)
        result = count_cycle_length(head)
        passed = result == expected
        all_passed = all_passed and passed
        
        status = "✓ PASS" if passed else "✗ FAIL"
        print(f"\nTest {i}: {status}")
        print(f"  Input: {values}, cycle at position {pos}")
        print(f"  Expected cycle length: {expected}")
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

