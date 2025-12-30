# Reverse Nodes In Even Length Groups

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_k(_head, k):
    curr = _head
    prev = None
    nxt = None

    for _ in range(k):
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    return prev, curr


def reverse_even_length_groups(head):
    # 1. 建立 dummy，並讓它指向原本的 head
    dummy = ListNode(0)
    dummy.next = head

    prev = dummy      # prev 指向「當前群組」的前驅
    l = 1             # 從群組大小 = 1,2,3,… 開始

    # 2. 只要後面還有節點，就持續找下一群組
    while prev.next:
        # 2.1 計算實際落在這個群組裡的節點數 n，並找到 node 指到群組的最後一個節點
        node = prev
        n = 0
        for _ in range(l):
            if not node.next:
                break
            node = node.next
            n += 1

        # 2.2 如果是偶數長度，就 in-place 反轉這 n 個節點
        if n % 2 == 0:
            curr = prev.next
            rev_head, nxt_node = reverse_k(prev.next, n)

            # 2.3 接回鍊表
            prev.next = rev_head
            curr.next = nxt_node
            prev = curr
        else:
            # 2.4 長度為奇數，不反轉；直接把 prev 推到群組末尾
            for _ in range(n):
                prev = prev.next

        # 2.5 群組大小遞增
        l += 1

    # 3. 回傳 dummy.next，即調整後的 head
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
        ([1, 2, 3, 4, 5, 6, 7], [1, 3, 2, 4, 5, 6, 7]),  # Groups: [1](odd), [2,3](even,reverse), [4,5,6](odd), [7](odd)
        ([1, 2, 3, 4, 5], [1, 3, 2, 5, 4]),  # Groups: [1](odd), [2,3](even,reverse), [4,5](even,reverse)
        ([1], [1]),
        ([1, 2], [1, 2]),
        ([0, 4, 2, 1, 3], [0, 2, 4, 3, 1]),  # Groups: [0](odd), [4,2](even,reverse), [1,3](even,reverse)
    ]
    
    print("Testing Reverse Nodes In Even Length Groups:")
    all_passed = True
    for i, (arr, expected) in enumerate(test_cases, 1):
        head = create_linked_list(arr)
        result_head = reverse_even_length_groups(head)
        result = linked_list_to_list(result_head)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status} reverse_even_length_groups({arr}) = {result}, expected {expected}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

