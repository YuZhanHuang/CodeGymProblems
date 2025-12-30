# Reverse Linked List II

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_node(start, count):
    prev, curr = None, start
    for _ in range(count):
        nxt = curr.next
        curr.next = prev
        prev, curr = curr, nxt
    return prev, curr


def reverse_between(head, left, right):
    # 建立 dummy 節點，方便處理 head 也可能被反轉的情況
    dummy = ListNode(0)
    dummy.next = head

    # prev 指到要反轉區間的前一個節點
    prev = dummy
    for _ in range(left - 1):
        prev = prev.next

    # 反轉 [left, right] 節點
    new_head, next_node = reverse_node(prev.next, right - left + 1)

    # 接回前後鏈
    tail = prev.next    # 原本的第 left 節點，現在是區段尾
    prev.next = new_head
    tail.next = next_node

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
        ([1, 2, 3, 4, 5], 2, 4, [1, 4, 3, 2, 5]),
        ([5], 1, 1, [5]),
        ([1, 2, 3], 1, 2, [2, 1, 3]),
        ([1, 2, 3, 4, 5], 1, 5, [5, 4, 3, 2, 1]),
    ]
    
    print("Testing Reverse Linked List II:")
    all_passed = True
    for i, (arr, left, right, expected) in enumerate(test_cases, 1):
        head = create_linked_list(arr)
        result_head = reverse_between(head, left, right)
        result = linked_list_to_list(result_head)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status} reverse_between({arr}, {left}, {right}) = {result}, expected {expected}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

