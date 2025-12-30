# Level Order Traversal of Binary Tree

from collections import deque


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def level_order_traversal(root):
    if not root:
        return "None"

    queue = deque()
    result = []
    queue.append(root)

    while queue:
        level_size = len(queue)
        level_nodes = []

        for _ in range(level_size):
            tmp = queue.popleft()
            level_nodes.append(str(tmp.data))

            if tmp.left:
                queue.append(tmp.left)
            if tmp.right:
                queue.append(tmp.right)
        
        result.append(", ".join(level_nodes))
    
    return " : ".join(result)


# Test cases
if __name__ == "__main__":
    # Test case 1: [1,2,3,4,5]
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.left.left = TreeNode(4)
    root1.left.right = TreeNode(5)
    root1.right = TreeNode(3)
    
    # Test case 2: Empty tree
    root2 = None
    
    # Test case 3: Single node
    root3 = TreeNode(1)
    
    test_cases = [
        (root1, "1 : 2, 3 : 4, 5"),
        (root2, "None"),
        (root3, "1"),
    ]
    
    print("Testing Level Order Traversal:")
    all_passed = True
    for i, (root, expected) in enumerate(test_cases, 1):
        result = level_order_traversal(root)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status} level_order_traversal(tree) = '{result}', expected '{expected}'")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

