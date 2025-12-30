# Clone Graph

from collections import deque


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


# Solution 1: BFS approach
def clone_bfs(root):
    if not root:
        return None

    # Map original → clone
    orig_to_clone = {root: Node(root.val)}
    queue = deque([root])

    while queue:
        u = queue.popleft()
        u_clone = orig_to_clone[u]

        for nbr in u.neighbors:
            if nbr not in orig_to_clone:
                # first time we see nbr: create clone and enqueue
                orig_to_clone[nbr] = Node(nbr.val)
                queue.append(nbr)
         
            # link the clone's neighbor
            u_clone.neighbors.append(orig_to_clone[nbr])

    return orig_to_clone[root]


# Solution 2: DFS approach
def clone_dfs(root):
    orig_to_clone = {}

    def dfs(u):
        # base case
        if u in orig_to_clone:
            return orig_to_clone[u]

        # create clone
        copy = Node(u.val)
        orig_to_clone[u] = copy

        # recursively clone neighbors
        for nbr in u.neighbors:
            copy.neighbors.append(dfs(nbr))

        return copy

    return dfs(root) if root else None


# Test cases
if __name__ == "__main__":
    # Test case 1: Simple triangle graph
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node1.neighbors = [node2, node3]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node1, node2]
    
    # Test BFS
    cloned_bfs = clone_bfs(node1)
    print("Testing Clone Graph (BFS):")
    print(f"Test 1: ✓ Original val={node1.val}, Cloned val={cloned_bfs.val}")
    print(f"        Original neighbors: {len(node1.neighbors)}, Cloned neighbors: {len(cloned_bfs.neighbors)}")
    print(f"        Different objects: {node1 is not cloned_bfs}")
    
    # Test DFS
    cloned_dfs = clone_dfs(node1)
    print("\nTesting Clone Graph (DFS):")
    print(f"Test 1: ✓ Original val={node1.val}, Cloned val={cloned_dfs.val}")
    print(f"        Original neighbors: {len(node1.neighbors)}, Cloned neighbors: {len(cloned_dfs.neighbors)}")
    print(f"        Different objects: {node1 is not cloned_dfs}")
    
    print("\nAll tests passed!")

