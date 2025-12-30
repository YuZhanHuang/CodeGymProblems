# Split Linked List in Parts

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def split_list_to_parts(head, k):
    # 1. 算整條 list 長度 n
    n = 0
    node = head
    while node:
        n += 1
        node = node.next

    # 2. 計算每段的基礎大小 base，以及前 extra 段要多拿 1 個節點
    base = n // k
    extra = n % k

    parts = [None] * k
    curr = head

    # 3. 按照前面計算的大小，把節點切下來接到 parts[i]
    for i in range(k):
        if not curr:
            # 節點不夠的情況就留 None
            parts[i] = None
            continue

        parts[i] = curr
        # 這一段該走的節點數
        sz = base + (1 if i < extra else 0)
        # 走到這段的最後一個節點
        for _ in range(sz - 1):
            curr = curr.next

        # 切斷
        nxt = curr.next
        curr.next = None
        curr = nxt

    return parts


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
        ([1, 2, 3], 5, [[1], [2], [3], [], []]),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3, [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]),
        ([1, 2, 3, 4, 5], 3, [[1, 2], [3, 4], [5]]),
        ([], 3, [[], [], []]),
    ]
    
    print("Testing Split Linked List in Parts:")
    all_passed = True
    for i, (arr, k, expected_parts) in enumerate(test_cases, 1):
        head = create_linked_list(arr)
        result_parts = split_list_to_parts(head, k)
        result = [linked_list_to_list(part) for part in result_parts]
        status = "✓" if result == expected_parts else "✗"
        if result != expected_parts:
            all_passed = False
        print(f"Test {i}: {status}")
        if result != expected_parts:
            print(f"  Input:    {arr}, k={k}")
            print(f"  Output:   {result}")
            print(f"  Expected: {expected_parts}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

