# Remove Duplicates from Sorted List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove_duplicates(head):
    curr = head
    while curr is not None:
        duplicate = curr.next
        while duplicate and duplicate.val == curr.val:
            duplicate = duplicate.next
        
        curr.next = duplicate
        curr = curr.next
    
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
        ([1, 1, 2], [1, 2]),
        ([1, 1, 2, 3, 3], [1, 2, 3]),
        ([1, 1, 1], [1]),
        ([1, 2, 3], [1, 2, 3]),
        ([], []),
        ([1], [1]),
    ]
    
    print("Testing Remove Duplicates from Sorted List:")
    all_passed = True
    for i, (arr, expected) in enumerate(test_cases, 1):
        head = create_linked_list(arr)
        result_head = remove_duplicates(head)
        result = linked_list_to_list(result_head)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status} remove_duplicates({arr}) = {result}, expected {expected}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

