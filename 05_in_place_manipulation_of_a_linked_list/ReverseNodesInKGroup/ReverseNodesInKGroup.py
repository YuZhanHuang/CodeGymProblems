# Reverse Nodes in k-Group

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_k(_head, k):
    cur = _head
    pre, nxt = None, None

    for _ in range(k):
        nxt = cur.next
        cur.next = pre
        pre = cur
        cur = nxt

    return pre, cur

            
def reverse_k_groups(head, k):
    dummy = ListNode(0)
    dummy.next = head
    ptr = dummy
    tracker = None

    while ptr is not None:
        tracker = ptr

        for _ in range(k):
            tracker = tracker.next

            if tracker is None:
                break
        
        if tracker is None:
            break

        prev, curr = reverse_k(ptr.next, k)
        last_node_head_ptr = ptr.next
        last_node_head_ptr.next = curr

        ptr.next = prev
        ptr = last_node_head_ptr

    return dummy.next


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
        ([1, 2, 3, 4, 5], 2, [2, 1, 4, 3, 5]),
        ([1, 2, 3, 4, 5], 3, [3, 2, 1, 4, 5]),
        ([1, 2, 3, 4, 5], 1, [1, 2, 3, 4, 5]),
        ([1, 2, 3, 4, 5], 5, [5, 4, 3, 2, 1]),
        ([1], 1, [1]),
    ]
    
    print("Testing Reverse Nodes in k-Group:")
    all_passed = True
    for i, (arr, k, expected) in enumerate(test_cases, 1):
        head = create_linked_list(arr)
        result_head = reverse_k_groups(head, k)
        result = linked_list_to_list(result_head)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status} reverse_k_groups({arr}, {k}) = {result}, expected {expected}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

