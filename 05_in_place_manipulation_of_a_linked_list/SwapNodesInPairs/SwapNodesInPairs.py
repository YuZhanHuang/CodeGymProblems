# Swap Nodes in Pairs

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_k(_head, k):
    curr = _head
    prev = None

    for _ in range(k):
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    return prev, curr


def swap_pairs(head):
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy

    while prev.next:
        node = prev

        for _ in range(2):
            if node.next:
                node = node.next
            else:
                return dummy.next

        curr = prev.next
        rev_head, left_head = reverse_k(prev.next, 2)
        
        prev.next = rev_head
        curr.next = left_head

        prev = curr
        curr = left_head

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
        ([1, 2, 3, 4], [2, 1, 4, 3]),
        ([1], [1]),
        ([], []),
        ([1, 2, 3], [2, 1, 3]),
    ]
    
    print("Testing Swap Nodes in Pairs:")
    all_passed = True
    for i, (arr, expected) in enumerate(test_cases, 1):
        head = create_linked_list(arr)
        result_head = swap_pairs(head)
        result = linked_list_to_list(result_head)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status} swap_pairs({arr}) = {result}, expected {expected}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

