# Binary Tree Zigzag Level Order Traversal

from collections import deque


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def zigzag_level_order(root):
    if not root:
        return []

    queue = deque()
    result = []
    queue.append(root)
    level = 1

    while queue:
        level_nodes = deque()
        queue_len = len(queue)

        for _ in range(queue_len):
            node = queue.popleft()
            if level % 2 == 0:
                level_nodes.appendleft(node.data)
            else:
                level_nodes.append(node.data)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(list(level_nodes))
        level += 1

    return result


# Test cases
if __name__ == "__main__":
    # Test case 1: [3,9,20,null,null,15,7]
    #       3
    #      / \
    #     9  20
    #       /  \
    #      15   7
    # Output: [[3],[20,9],[15,7]]
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)
    
    # Test case 2: [1]
    root2 = TreeNode(1)
    
    # Test case 3: []
    root3 = None
    
    test_cases = [
        (root1, [[3], [20, 9], [15, 7]]),
        (root2, [[1]]),
        (root3, []),
    ]
    
    print("Testing Zigzag Level Order Traversal:")
    all_passed = True
    for i, (root, expected) in enumerate(test_cases, 1):
        result = zigzag_level_order(root)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status} zigzag_level_order(tree) = {result}, expected {expected}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

