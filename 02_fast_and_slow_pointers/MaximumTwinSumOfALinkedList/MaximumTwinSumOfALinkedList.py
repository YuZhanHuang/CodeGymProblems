from utils.data_structures import create_linked_list


def twin_sum(head):
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    curr = slow
    prev = None

    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    curr = head
    max_sum = 0

    while prev:
        max_sum = max(max_sum, curr.val + prev.val)
        curr = curr.next
        prev = prev.next

    return max_sum


def main():
    """Test cases for Maximum Twin Sum of a Linked List"""
    test_cases = [
        # (values, expected_max_sum, description)
        ([5, 4, 2, 1], 6, "Max twin sum is 5+1=6"),
        ([4, 2, 2, 3], 7, "Max twin sum is 4+3=7"),
        ([1, 100000], 100001, "Two nodes, sum is 100001"),
        ([1, 2, 3, 4], 5, "Max twin sum is 1+4=5 or 2+3=5"),
        ([10, 20, 30, 40, 50, 60], 70, "Max twin sum is 10+60=70"),
    ]

    print("=" * 70)
    print("Testing: Maximum Twin Sum of a Linked List")
    print("=" * 70)

    all_passed = True
    for i, (values, expected, description) in enumerate(test_cases, 1):
        head = create_linked_list(values)
        result = twin_sum(head)
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
