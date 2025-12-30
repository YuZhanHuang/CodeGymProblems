# House Robber III

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def rob(root):
    return max(heist(root))


def heist(root):
    if root is None:
        return [0, 0]
    
    left_subtree = heist(root.left)
    right_subtree = heist(root.right)
    
    include_root = root.data + left_subtree[1] + right_subtree[1]
    exclude_root = max(left_subtree) + max(right_subtree)
    
    return [include_root, exclude_root]


# Helper function to build tree
def build_tree(values):
    if not values:
        return None
    
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    
    while queue and i < len(values):
        node = queue.pop(0)
        
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    
    return root


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([3, 2, 3, None, 3, None, 1], 7),
        ([3, 4, 5, 1, 3, None, 1], 9),
        ([1], 1),
    ]
    
    print("Testing House Robber III:")
    all_passed = True
    for i, (values, expected) in enumerate(test_cases, 1):
        root = build_tree(values)
        result = rob(root)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status} rob(tree) = {result}, expected {expected}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

