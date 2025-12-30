# Symmetric Tree

from collections import deque


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def is_symmetric(root):
    if not root:
        return True
    
    queue = deque([(root.left, root.right)])
    
    while queue:
        left, right = queue.popleft()
        if not left and not right:
            continue
        if not left or not right:
            return False
        if left.data != right.data:
            return False
        
        queue.append((left.left, right.right))
        queue.append((left.right, right.left))
    
    return True


# Test cases
if __name__ == "__main__":
    # Test case 1: Symmetric tree [1,2,2,3,4,4,3]
    #       1
    #      / \
    #     2   2
    #    / \ / \
    #   3  4 4  3
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.left.left = TreeNode(3)
    root1.left.right = TreeNode(4)
    root1.right = TreeNode(2)
    root1.right.left = TreeNode(4)
    root1.right.right = TreeNode(3)
    
    # Test case 2: Not symmetric [1,2,2,null,3,null,3]
    #     1
    #    / \
    #   2   2
    #    \   \
    #     3   3
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.left.right = TreeNode(3)
    root2.right = TreeNode(2)
    root2.right.right = TreeNode(3)
    
    test_cases = [
        (root1, True),
        (root2, False),
    ]
    
    print("Testing Symmetric Tree:")
    all_passed = True
    for i, (root, expected) in enumerate(test_cases, 1):
        result = is_symmetric(root)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status} is_symmetric(tree) = {result}, expected {expected}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

