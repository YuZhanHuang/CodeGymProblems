from utils.data_structures import create_linked_list_with_cycle


def detect_cycle(head):
   slow, fast = head, head
   if head is None:
      return False

   while fast and fast.next:
      slow = slow.next
      fast = fast.next.next
     
      if slow == fast:
         return True

   return False


def main():
    """Test cases for Linked List Cycle"""
    test_cases = [
        # (values, cycle_pos, expected_output, description)
        ([3, 2, 0, -4], 1, True, "Cycle at position 1 (value 2)"),
        ([1, 2], 0, True, "Cycle at head"),
        ([1], -1, False, "Single node, no cycle"),
        ([1, 2, 3, 4, 5], -1, False, "No cycle in list"),
        ([1, 2, 3], 2, True, "Cycle at last node"),
    ]
    
    print("=" * 70)
    print("Testing: Linked List Cycle")
    print("=" * 70)
    
    all_passed = True
    for i, (values, pos, expected, description) in enumerate(test_cases, 1):
        head = create_linked_list_with_cycle(values, pos)
        result = detect_cycle(head)
        passed = result == expected
        all_passed = all_passed and passed
        
        status = "✓ PASS" if passed else "✗ FAIL"
        print(f"\nTest {i}: {status}")
        print(f"  Input: {values}, cycle at position {pos}")
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

