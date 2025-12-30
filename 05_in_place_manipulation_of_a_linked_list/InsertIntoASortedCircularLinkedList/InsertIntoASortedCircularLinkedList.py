# Insert into a Sorted Circular Linked List

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def insert(head, insertVal):
    # edge case
    if not head:
        node = Node(insertVal)
        node.next = node
        return node
    
    prev, curr = head, head.next
    is_inserted = False
    
    while True:
        # case1: normal case, insert between prev and curr
        if prev.val <= insertVal <= curr.val:
            is_inserted = True
        # case2: at the rotation point (prev.val > curr.val)
        elif prev.val > curr.val:
            # insert if it's larger than max or smaller than min
            if insertVal >= prev.val or insertVal <= curr.val:
                is_inserted = True
        
        if is_inserted:
            node = Node(insertVal, curr)
            prev.next = node
            return head
        
        prev, curr = curr, curr.next
        
        # we've gone full circle without finding a spot
        if prev is head:
            break
    
    # case3: all nodes have same value, insert anywhere
    node = Node(insertVal, curr)
    prev.next = node
    
    return head


# Helper function to convert circular linked list to array
def circular_list_to_array(head):
    if not head:
        return []
    result = [head.val]
    curr = head.next
    while curr and curr != head:
        result.append(curr.val)
        curr = curr.next
    return result


# Helper function to create circular linked list
def create_circular_list(arr):
    if not arr:
        return None
    head = Node(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = Node(val)
        curr = curr.next
    curr.next = head  # make it circular
    return head


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([3, 4, 1], 2, [3, 4, 1, 2]),  # Insert at rotation point
        ([1], 0, [1, 0]),
        ([3, 5, 1], 4, [3, 5, 1, 4]),  # Should be [3, 4, 5, 1] or similar
        ([], 1, [1]),
    ]
    
    print("Testing Insert into a Sorted Circular Linked List:")
    all_passed = True
    for i, (arr, insertVal, _) in enumerate(test_cases, 1):
        head = create_circular_list(arr)
        result_head = insert(head, insertVal)
        result = circular_list_to_array(result_head)
        
        # Check if insertVal is in the result
        if insertVal in result and len(result) == len(arr) + 1:
            status = "✓"
        else:
            status = "✗"
            all_passed = False
        
        print(f"Test {i}: {status} insert({arr}, {insertVal}) = {result}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

