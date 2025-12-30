# Vertical Order Traversal of a Binary Tree

from collections import defaultdict, deque


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def vertical_order(root):
    if root is None:
        return []
    
    check_cols = defaultdict(list)
    queue = deque()
    queue.append((root, 0))
    min_col, max_col = 0, 0

    while queue:
        current, col = queue.popleft()

        if current is not None:
            check_cols[col].append(current.data)

            min_col = min(min_col, col)
            max_col = max(max_col, col)

            queue.append((current.left, col - 1))
            queue.append((current.right, col + 1))

    return [check_cols[i] for i in range(min_col, max_col+1)]


# Test cases
if __name__ == "__main__":
    # Test case 1: [3,9,20,null,null,15,7]
    #       3
    #      / \
    #     9  20
    #       /  \
    #      15   7
    # Vertical order: [[9],[3,15],[20],[7]]
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)
    
    # Test case 2: [3,9,8,4,0,1,7]
    #         3
    #        / \
    #       9   8
    #      / \ / \
    #     4  0 1  7
    # Vertical order: [[4],[9],[3,0,1],[8],[7]]
    root2 = TreeNode(3)
    root2.left = TreeNode(9)
    root2.left.left = TreeNode(4)
    root2.left.right = TreeNode(0)
    root2.right = TreeNode(8)
    root2.right.left = TreeNode(1)
    root2.right.right = TreeNode(7)
    
    test_cases = [
        (root1, [[9], [3, 15], [20], [7]]),
        (root2, [[4], [9], [3, 0, 1], [8], [7]]),
    ]
    
    print("Testing Vertical Order Traversal:")
    all_passed = True
    for i, (root, expected) in enumerate(test_cases, 1):
        result = vertical_order(root)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status} vertical_order(tree) = {result}")
        print(f"        expected {expected}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

