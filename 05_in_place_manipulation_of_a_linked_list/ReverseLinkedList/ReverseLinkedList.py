# Reverse Linked List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse(head):
    cur = head
    pre = None
    nxt = None

    while cur is not None:
        nxt = cur.next
        cur.next = pre
        pre = cur
        cur = nxt
    
    return pre


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
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
        ([1, 2], [2, 1]),
        ([1], [1]),
        ([1, 2, 3], [3, 2, 1]),
        ([], []),
    ]
    
    print("Testing Reverse Linked List:")
    all_passed = True
    for i, (arr, expected) in enumerate(test_cases, 1):
        head = create_linked_list(arr)
        result_head = reverse(head)
        result = linked_list_to_list(result_head)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status} reverse({arr}) = {result}, expected {expected}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

