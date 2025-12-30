# Lowest Common Ancestor in a Binary Tree


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def lowestCommonAncestor(root, p, q):
    def dfs(node):
        # base case
        if not node or node.val == p.val or node.val == q.val:
            return node

        left = dfs(node.left)
        right = dfs(node.right)

        if left and right:
            return node
        
        return left if left else right

    return dfs(root)


# Test cases
if __name__ == "__main__":
    # Test case 1: [3,5,1,6,2,0,8,null,null,7,4]
    #        3
    #       / \
    #      5   1
    #     / \ / \
    #    6  2 0  8
    #      / \
    #     7   4
    # p=5, q=1, LCA=3
    root1 = TreeNode(3)
    root1.left = TreeNode(5)
    root1.right = TreeNode(1)
    root1.left.left = TreeNode(6)
    root1.left.right = TreeNode(2)
    root1.right.left = TreeNode(0)
    root1.right.right = TreeNode(8)
    root1.left.right.left = TreeNode(7)
    root1.left.right.right = TreeNode(4)
    
    p1 = root1.left  # 5
    q1 = root1.right  # 1
    
    # Test case 2: same tree, p=5, q=4, LCA=5
    p2 = root1.left  # 5
    q2 = root1.left.right.right  # 4
    
    test_cases = [
        (root1, p1, q1, 3),
        (root1, p2, q2, 5),
    ]
    
    print("Testing Lowest Common Ancestor:")
    all_passed = True
    for i, (root, p, q, expected_val) in enumerate(test_cases, 1):
        result = lowestCommonAncestor(root, p, q)
        result_val = result.val if result else None
        status = "✓" if result_val == expected_val else "✗"
        if result_val != expected_val:
            all_passed = False
        print(f"Test {i}: {status} lowestCommonAncestor(tree, p={p.val}, q={q.val}) = {result_val}, expected {expected_val}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

