# Remove Linked List Elements

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove_elements(head, k):
    dummy = ListNode(0)
    dummy.next = head
    
    prev = dummy
    curr = head
    
    while curr is not None:
        if curr.val == k:
            nxt = curr.next
            curr.next = None
            prev.next = nxt
            curr = nxt
        else:
            prev = curr
            curr = curr.next
    
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
        ([1, 2, 6, 3, 4, 5, 6], 6, [1, 2, 3, 4, 5]),
        ([7, 7, 7, 7], 7, []),
        ([1, 2, 3], 4, [1, 2, 3]),
        ([], 1, []),
        ([1], 1, []),
        ([1, 2], 1, [2]),
    ]
    
    print("Testing Remove Linked List Elements:")
    all_passed = True
    for i, (arr, k, expected) in enumerate(test_cases, 1):
        head = create_linked_list(arr)
        result_head = remove_elements(head, k)
        result = linked_list_to_list(result_head)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status} remove_elements({arr}, {k}) = {result}, expected {expected}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

