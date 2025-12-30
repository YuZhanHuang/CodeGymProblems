# Populating Next Right Pointers in Each Node

from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.next = None


# Solution 1: BFS with Queue (O(n) time, O(n) space)
def populate_next_pointers_bfs(root):
    if not root:
        return root
    
    queue = deque()
    queue.append(root)

    while queue:
        queue_len = len(queue)
        for i in range(queue_len):
            node = queue.popleft()
            node.next = queue[0] if queue and i < queue_len - 1 else None
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return root


# Solution 2: Level-by-level traversal (O(n) time, O(1) space)
def populate_next_pointers(root):
    if not root:
        return root

    mostleft = root 

    while mostleft.left:
        current = mostleft

        while current:
            current.left.next = current.right

            if current.next:
                current.right.next = current.next.left

            current = current.next

        mostleft = mostleft.left

    return root


def get_next_pointers(root):
    """Helper: get all next pointers for testing"""
    if not root:
        return []
    
    result = []
    level_start = root
    
    while level_start:
        current = level_start
        level_nexts = []
        while current:
            level_nexts.append(current.next.data if current.next else None)
            current = current.next
        result.append(level_nexts)
        level_start = level_start.left
    
    return result


# Test cases
if __name__ == "__main__":
    # Test case 1: Perfect binary tree [1,2,3,4,5,6,7]
    #         1
    #        / \
    #       2   3
    #      / \ / \
    #     4  5 6  7
    root1 = Node(1)
    root1.left = Node(2)
    root1.right = Node(3)
    root1.left.left = Node(4)
    root1.left.right = Node(5)
    root1.right.left = Node(6)
    root1.right.right = Node(7)
    
    # Test BFS approach
    populate_next_pointers_bfs(root1)
    result1 = get_next_pointers(root1)
    expected1 = [[None], [3, None], [5, 6, 7, None]]
    
    # Test case 2 for O(1) space approach
    root2 = Node(1)
    root2.left = Node(2)
    root2.right = Node(3)
    root2.left.left = Node(4)
    root2.left.right = Node(5)
    root2.right.left = Node(6)
    root2.right.right = Node(7)
    
    populate_next_pointers(root2)
    result2 = get_next_pointers(root2)
    
    print("Testing Populating Next Right Pointers:")
    print(f"Test 1 (BFS): {'✓' if result1 == expected1 else '✗'} {result1}")
    print(f"Test 2 (O(1) space): {'✓' if result2 == expected1 else '✗'} {result2}")
    
    all_passed = result1 == expected1 and result2 == expected1
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

