from utils.data_structures import (
    circular_linked_list_to_list,
    create_circular_linked_list,
)


def split_circular_linked_list(head):
    if not head or head.next == head:
        return [head, None]

    slow, fast = head, head

    # 1) Walk until fast would wrap around
    while fast.next != head and fast.next.next != head:
        slow = slow.next
        fast = fast.next.next

    # 2) Advance split by one to guarantee ⌈n/2⌉ in first half
    prev = slow
    slow = slow.next

    # 3) Close first half into a circle
    prev.next = head

    # 4) Close second half into a circle
    curr = slow
    while curr.next != head:
        curr = curr.next
    curr.next = slow

    return [head, slow]


def main():
    """Test cases for Split a Circular Linked List"""
    test_cases = [
        # (values, expected_first_half_len, expected_second_half_len, description)
        ([1, 2, 3, 4, 5], 3, 2, "5 nodes: first 3, second 2"),
        ([1, 2, 3, 4], 2, 2, "4 nodes: first 2, second 2"),
        ([1, 2], 1, 1, "2 nodes: first 1, second 1"),
        ([1, 2, 3], 2, 1, "3 nodes: first 2, second 1"),
        ([1, 2, 3, 4, 5, 6], 3, 3, "6 nodes: first 3, second 3"),
    ]

    print("=" * 70)
    print("Testing: Split a Circular Linked List")
    print("=" * 70)

    all_passed = True
    for i, (values, exp_len1, exp_len2, description) in enumerate(test_cases, 1):
        head = create_circular_linked_list(values)
        result = split_circular_linked_list(head)

        first_list = circular_linked_list_to_list(result[0], exp_len1)
        second_list = (
            circular_linked_list_to_list(result[1], exp_len2) if result[1] else []
        )

        # Verify the split is correct
        passed = (
            len(first_list) == exp_len1
            and len(second_list) == exp_len2
            and first_list + second_list == values
        )
        all_passed = all_passed and passed

        status = "✓ PASS" if passed else "✗ FAIL"
        print(f"\nTest {i}: {status}")
        print(f"  Input: {values}")
        print(f"  First half: {first_list} (length {len(first_list)})")
        print(f"  Second half: {second_list} (length {len(second_list)})")
        print(f"  Expected: first={exp_len1}, second={exp_len2}")
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
