# Delete N Nodes After M Nodes of a Linked List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def delete_nodes(head, m, n):
    current = head
    last_m_node = head

    while current:
        m_count = m
        while current and m_count > 0:
            last_m_node = current
            current = current.next
            m_count -= 1

        n_count = n
        while current and n_count > 0:
            current = current.next
            n_count -= 1

        last_m_node.next = current
    
    return head


# Helper functions
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linked_list_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], 2, 3, [1, 2, 6, 7, 11, 12]),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 1, 3, [1, 5, 9]),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3, 1, [1, 2, 3, 5, 6, 7, 9, 10]),
        ([9, 3, 7, 7, 9, 10, 8, 2], 1, 2, [9, 7, 8]),  # Keep 9, delete 3,7, keep 7, delete 9,10, keep 8, delete 2
    ]
    
    print("Testing Delete N Nodes After M Nodes of a Linked List:")
    all_passed = True
    for i, (arr, m, n, expected) in enumerate(test_cases, 1):
        head = create_linked_list(arr)
        result_head = delete_nodes(head, m, n)
        result = linked_list_to_list(result_head)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status} delete_nodes({arr}, {m}, {n}) = {result}, expected {expected}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

