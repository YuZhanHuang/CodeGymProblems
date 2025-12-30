# Maximum Depth of Binary Tree


class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


# Solution 1: Find Maximum Depth
def find_max_depth(root):
    max_depth = 0
    
    def depth_rec(node):
        nonlocal max_depth
        if not node:
            return 0
        ld = depth_rec(node.left)
        lr = depth_rec(node.right)
        
        depth = max(ld, lr) + 1
        max_depth = max(max_depth, depth)
        
        return depth
    
    depth_rec(root)
    return max_depth


# Solution 2: Find Minimum Depth
def minDepth(root):
    if not root:
        return 0
    ans = float('inf')

    def dfs(node, depth):
        nonlocal ans
        if not node:
            return
        if not node.left and not node.right:  # leaf node
            ans = min(ans, depth)
            return
        dfs(node.left, depth + 1)
        dfs(node.right, depth + 1)

    dfs(root, 1)
    return ans


# Test cases
if __name__ == "__main__":
    # Test case 1: [3,9,20,null,null,15,7]
    #       3
    #      / \
    #     9  20
    #       /  \
    #      15   7
    # Max depth: 3, Min depth: 2
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20, TreeNode(15), TreeNode(7))
    
    # Test case 2: [2,null,3,null,4,null,5,null,6]
    #   2
    #    \
    #     3
    #      \
    #       4
    #        \
    #         5
    #          \
    #           6
    # Max depth: 5, Min depth: 5
    root2 = TreeNode(2)
    root2.right = TreeNode(3)
    root2.right.right = TreeNode(4)
    root2.right.right.right = TreeNode(5)
    root2.right.right.right.right = TreeNode(6)
    
    print("Testing Maximum Depth of Binary Tree:")
    test_cases_max = [
        (root1, 3),
        (root2, 5),
    ]
    
    all_passed = True
    for i, (root, expected) in enumerate(test_cases_max, 1):
        result = find_max_depth(root)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i} (Max): {status} find_max_depth(tree) = {result}, expected {expected}")
    
    print("\nTesting Minimum Depth of Binary Tree:")
    test_cases_min = [
        (root1, 2),
        (root2, 5),
    ]
    
    for i, (root, expected) in enumerate(test_cases_min, 1):
        result = minDepth(root)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i} (Min): {status} minDepth(tree) = {result}, expected {expected}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

