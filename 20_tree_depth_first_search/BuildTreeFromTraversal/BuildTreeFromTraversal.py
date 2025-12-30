# Build Binary Tree from Preorder and Inorder Traversal


class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def depth_first_helper(p_order, i_order, left, right, mapping, p_index):
    if left > right:
        return None
    
    current = p_order[p_index[0]]
    p_index[0] += 1 
    root = TreeNode(current)

    if left == right:
        return root

    in_index = mapping[current]

    root.left = depth_first_helper(p_order, i_order, left, in_index-1, mapping, p_index)
    root.right = depth_first_helper(p_order, i_order, in_index+1, right, mapping, p_index)
    
    return root


def build_tree(p_order, i_order):
    mapping = {}
    p_index = [0]
    for i in range(len(i_order)):
        mapping[i_order[i]] = i

    return depth_first_helper(p_order, i_order, 0, len(i_order)-1, mapping, p_index)


def tree_to_inorder(root):
    """Helper: convert tree back to inorder list for verification"""
    result = []
    def inorder(node):
        if not node:
            return
        inorder(node.left)
        result.append(node.data)
        inorder(node.right)
    inorder(root)
    return result


def tree_to_preorder(root):
    """Helper: convert tree back to preorder list for verification"""
    result = []
    def preorder(node):
        if not node:
            return
        result.append(node.data)
        preorder(node.left)
        preorder(node.right)
    preorder(root)
    return result


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([3, 9, 20, 15, 7], [9, 3, 15, 20, 7]),
        ([1, 2], [2, 1]),
    ]
    
    print("Testing Build Tree from Traversal:")
    all_passed = True
    for i, (p_order, i_order) in enumerate(test_cases, 1):
        root = build_tree(p_order, i_order)
        result_pre = tree_to_preorder(root)
        result_in = tree_to_inorder(root)
        pre_ok = result_pre == p_order
        in_ok = result_in == i_order
        status = "✓" if pre_ok and in_ok else "✗"
        if not (pre_ok and in_ok):
            all_passed = False
        print(f"Test {i}: {status} build_tree(preorder={p_order}, inorder={i_order})")
        print(f"       Reconstructed preorder={result_pre}, inorder={result_in}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

