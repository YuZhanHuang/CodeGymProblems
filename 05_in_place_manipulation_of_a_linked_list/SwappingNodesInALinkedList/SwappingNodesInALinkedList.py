# Swapping Nodes in a Linked List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swap(node1, node2):
    temp = node1.val
    node1.val = node2.val
    node2.val = temp

            
def swap_nodes(head, k):
    cur = head
    end = None
    start = None

    for _ in range(k-1):
        cur = cur.next

    start = cur
    end = head

    while cur and cur.next:
        cur = cur.next
        end = end.next
    
    swap(start, end)
    
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
        ([1, 2, 3, 4, 5], 2, [1, 4, 3, 2, 5]),
        ([7, 9, 6, 6, 7, 8, 3, 0, 9, 5], 5, [7, 9, 6, 6, 8, 7, 3, 0, 9, 5]),
        ([1], 1, [1]),
        ([1, 2], 1, [2, 1]),
        ([1, 2, 3], 2, [1, 2, 3]),
    ]
    
    print("Testing Swapping Nodes in a Linked List:")
    all_passed = True
    for i, (arr, k, expected) in enumerate(test_cases, 1):
        head = create_linked_list(arr)
        result_head = swap_nodes(head, k)
        result = linked_list_to_list(result_head)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status} swap_nodes({arr}, {k}) = {result}, expected {expected}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

