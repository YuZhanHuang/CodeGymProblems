# Reorder List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reorder(head):
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    second = slow.next
    slow.next = None

    prev = None

    while second is not None:
        nxt = second.next
        second.next = prev
        prev = second
        second = nxt

    t1 = head
    t2 = prev

    while t2:
        t1_nxt = t1.next
        t2_nxt = t2.next
        t1.next = t2
        t2.next = t1_nxt
        t1 = t1_nxt
        t2 = t2_nxt

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
        ([1, 2, 3, 4], [1, 4, 2, 3]),
        ([1, 2, 3, 4, 5], [1, 5, 2, 4, 3]),
        ([1], [1]),
        ([1, 2], [1, 2]),
    ]
    
    print("Testing Reorder List:")
    all_passed = True
    for i, (arr, expected) in enumerate(test_cases, 1):
        head = create_linked_list(arr)
        result_head = reorder(head)
        result = linked_list_to_list(result_head)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status} reorder({arr}) = {result}, expected {expected}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

