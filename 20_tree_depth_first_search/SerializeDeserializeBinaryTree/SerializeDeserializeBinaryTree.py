# Serialize and Deserialize Binary Tree


class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


NULL = 1001  # sentinel; not in [-1000, 1000] range


def serialize(root):
    out = []
    def dfs(node):
        if node is None:
            out.append(NULL)
            return
        out.append(node.data)
        dfs(node.left)
        dfs(node.right)
    dfs(root)
    return out


def deserialize(nums):
    it = iter(nums)
    def dfs():
        try:
            val = next(it)
        except StopIteration:
            return None
        if val == NULL:
            return None
        node = TreeNode(val)
        node.left = dfs()
        node.right = dfs()
        return node
    return dfs()


def is_same_tree(a, b):
    if a is b:   # same object or both None
        return True
    if not a or not b:
        return False
    return (
        a.data == b.data and
        is_same_tree(a.left, b.left) and
        is_same_tree(a.right, b.right)
    )


def pretty_preorder(root):
    """Human-readable (with NULL) preorder output for observation"""
    res = []
    def dfs(n):
        if n is None:
            res.append("∅")
            return
        res.append(str(n.data))
        dfs(n.left)
        dfs(n.right)
    dfs(root)
    return " ".join(res)


# Test cases
if __name__ == "__main__":
    cases = []

    # 1) Empty tree
    cases.append(("empty", None))

    # 2) Single node
    cases.append(("single", TreeNode(0)))

    # 3) Complete binary tree
    #        1
    #       / \
    #      2   3
    cases.append(("perfect-3", TreeNode(1, TreeNode(2), TreeNode(3))))

    # 4) Mixed null subtrees
    #        1
    #       / \
    #      2   3
    #     /   / \
    #    ∅   ∅   4
    cases.append((
        "mixed-nulls",
        TreeNode(1, TreeNode(2, None, None), TreeNode(3, None, TreeNode(4)))
    ))

    # 5) Left-skewed tree
    #    5
    #   /
    #  4
    # /
    #3
    cases.append(("left-skew", TreeNode(5, TreeNode(4, TreeNode(3)))))

    # 6) With negative and boundary values
    #        -1
    #       /   \
    #   -1000   1000
    cases.append(("neg-and-bound", TreeNode(-1, TreeNode(-1000), TreeNode(1000))))

    # Execute tests
    print("Testing Serialize and Deserialize Binary Tree:")
    all_passed = True
    for name, root in cases:
        arr = serialize(root)
        rebuilt = deserialize(arr)

        ok_same = is_same_tree(root, rebuilt)
        arr2 = serialize(rebuilt)
        ok_idempotent = (arr2 == arr)

        status = "✓" if ok_same and ok_idempotent else "✗"
        if not ok_same or not ok_idempotent:
            all_passed = False
            print(f"Test [{name}]: {status} same_tree={ok_same}, idempotent={ok_idempotent}")
            print(f"  Original:  {pretty_preorder(root)}")
            print(f"  Rebuilt:   {pretty_preorder(rebuilt)}")
        else:
            print(f"Test [{name}]: {status}")

    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

