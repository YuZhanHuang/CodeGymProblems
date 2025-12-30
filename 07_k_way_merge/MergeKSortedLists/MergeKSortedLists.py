# Merge K Sorted Lists

from heapq import *


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_k_lists(lists):
    n = len(lists)
    min_heap = []
    
    for i in range(n):
        if lists[i]:
            heappush(min_heap, (lists[i].val, i, lists[i]))
    
    curr = min_heap[0][2] if min_heap else None
    dummy = ListNode(0)
    dummy.next = curr
    
    while min_heap:
        nxt_val, nxt_idx, nxt_node = heappop(min_heap)
        if curr == nxt_node:
            if nxt_node.next:
                heappush(min_heap, (nxt_node.next.val, nxt_idx, nxt_node.next))
            continue
        
        curr.next = nxt_node
        curr = nxt_node
        if nxt_node.next:
            heappush(min_heap, (nxt_node.next.val, nxt_idx, nxt_node.next))
    
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
        ([[1, 4, 5], [1, 3, 4], [2, 6]], [1, 1, 2, 3, 4, 4, 5, 6]),
        ([], []),
        ([[]], []),
        ([[1], [0]], [0, 1]),
    ]
    
    print("Testing Merge K Sorted Lists:")
    all_passed = True
    for i, (lists_data, expected) in enumerate(test_cases, 1):
        lists = [create_linked_list(arr) for arr in lists_data]
        result_head = merge_k_lists(lists)
        result = linked_list_to_list(result_head)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status} merge_k_lists({lists_data}) = {result}, expected {expected}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

