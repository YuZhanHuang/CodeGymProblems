# Remove nth Node from End of List

# Definition for a Linked List node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def remove_nth_last_node(head: ListNode, n: int) -> ListNode:
    # 1) Dummy head simplifies removal of the real head
    dummy = ListNode(0)
    dummy.next = head

    # 2) Initialize two pointers both at dummy
    fast = dummy
    slow = dummy

    # 3) Move fast ahead by n+1 steps so gap between fast & slow is n
    for _ in range(n + 1):
        fast = fast.next

    # 4) Move both until fast hits the end
    while fast:
        fast = fast.next
        slow = slow.next

    # 5) slow.next is the node to remove
    slow.next = slow.next.next

    # 6) Return the (possibly new) head
    return dummy.next


# Helper function to create linked list from list
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


# Helper function to convert linked list to list
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
        ([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]),
        ([1], 1, []),
        ([1, 2], 1, [1]),
        ([1, 2], 2, [2]),
        ([1, 2, 3, 4, 5], 5, [2, 3, 4, 5]),
        ([1, 2, 3, 4, 5], 1, [1, 2, 3, 4]),
        ([1, 2, 3], 3, [2, 3]),
    ]
    
    print("Testing Remove nth Node from End of List:")
    all_passed = True
    for i, (arr, n, expected) in enumerate(test_cases, 1):
        head = create_linked_list(arr)
        result_head = remove_nth_last_node(head, n)
        result = linked_list_to_list(result_head)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status} remove_nth_last_node({arr}, {n}) = {result}, expected {expected}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

