# Connect All Siblings of a Binary Tree

from collections import deque
import signal


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.next = None


class TimeoutError(Exception):
    pass


def timeout_handler(signum, frame):
    raise TimeoutError("Execution exceeded 10 seconds")


def connect_all_siblings(root):
    """
    Connect all nodes level by level, with the rightmost node of each level
    pointing to the first node of the next level.
    """
    if not root:
        return root
    
    # Use BFS to connect nodes level by level
    queue = deque([root])
    prev = None
    
    while queue:
        node = queue.popleft()
        
        # Connect previous node to current node
        if prev:
            prev.next = node
        prev = node
        
        # Add children to queue
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    # Last node's next should be None
    if prev:
        prev.next = None
    
    return root


def get_all_nexts(root):
    """Helper: traverse all next pointers with timeout protection"""
    if not root:
        return []
    
    result = []
    current = root
    visited = set()
    max_nodes = 1000  # Safety limit
    
    while current and len(result) < max_nodes:
        if current in visited:
            # Detected cycle, break
            break
        visited.add(current)
        result.append(current.data)
        current = current.next
    
    return result


# Test cases
if __name__ == "__main__":
    import sys
    
    try:
        # Set timeout for 10 seconds (Unix-based systems)
        if hasattr(signal, 'SIGALRM'):
            signal.signal(signal.SIGALRM, timeout_handler)
            signal.alarm(10)
        
        # Test case 1: Perfect binary tree [1,2,3,4,5,6,7]
        #         1
        #        / \
        #       2   3
        #      / \ / \
        #     4  5 6  7
        # Connected: 1->2->3->4->5->6->7->NULL
        root1 = Node(1)
        root1.left = Node(2)
        root1.right = Node(3)
        root1.left.left = Node(4)
        root1.left.right = Node(5)
        root1.right.left = Node(6)
        root1.right.right = Node(7)
        
        connect_all_siblings(root1)
        result1 = get_all_nexts(root1)
        expected1 = [1, 2, 3, 4, 5, 6, 7]
        
        # Cancel alarm
        if hasattr(signal, 'SIGALRM'):
            signal.alarm(0)
        
        print("Testing Connect All Siblings:")
        print(f"Test 1: {'✓' if result1 == expected1 else '✗'} {result1}")
        print(f"        expected {expected1}")
        
        all_passed = result1 == expected1
        print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")
        
    except TimeoutError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nExecution interrupted by user")
        sys.exit(1)

