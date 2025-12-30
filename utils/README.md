# Utils Module

This module contains reusable data structures and helper functions for CodeGym Problems.

## Structure

```
utils/
├── __init__.py
├── data_structures/
│   ├── __init__.py
│   └── linked_list.py
└── README.md
```

## Data Structures

### Linked List (`utils/data_structures/linked_list.py`)

Contains implementations for linked list operations:

- **`ListNode`**: Single node in a linked list
- **`create_linked_list(values)`**: Create a linked list from a list of values
- **`create_linked_list_with_cycle(values, pos)`**: Create a linked list with a cycle
- **`create_circular_linked_list(values)`**: Create a circular linked list
- **`linked_list_to_list(head, max_length)`**: Convert linked list to Python list
- **`circular_linked_list_to_list(head, num_nodes)`**: Convert circular linked list to Python list
- **`print_linked_list(head, max_length)`**: Print linked list for debugging

#### Usage Example

```python
from utils.data_structures import create_linked_list, ListNode

# Create a simple linked list
head = create_linked_list([1, 2, 3, 4, 5])

# Create a linked list with cycle
head_with_cycle = create_linked_list_with_cycle([1, 2, 3, 4], pos=1)

# Create a circular linked list
circular_head = create_circular_linked_list([1, 2, 3, 4])
```

## Future Data Structures

This module is designed to be extended with additional data structures:

- **Graph**: For graph-related problems (pattern 19)
- **Union Find (Disjoint Set)**: For union-find problems (pattern 25)
- **Trie**: For trie-related problems (pattern 22)
- **Binary Tree**: For tree traversal problems (patterns 20, 21)
- **Heap**: For heap-related problems (pattern 6)
- **Custom Data Structures**: For pattern 26

## Adding New Data Structures

To add a new data structure:

1. Create a new Python file in `utils/data_structures/`
2. Implement your data structure classes and helper functions
3. Update `utils/data_structures/__init__.py` to export the new classes/functions
4. Update this README with usage examples

Example for adding a Graph data structure:

```python
# utils/data_structures/graph.py
class GraphNode:
    def __init__(self, val=0):
        self.val = val
        self.neighbors = []

def create_graph(adjacency_list):
    # Implementation here
    pass
```

```python
# utils/data_structures/__init__.py
from .linked_list import (...)
from .graph import GraphNode, create_graph

__all__ = [
    # ... existing exports
    'GraphNode',
    'create_graph'
]
```

## Import Convention

Always use absolute imports from the project root:

```python
# ✓ Good
from utils.data_structures import create_linked_list

# ✗ Bad - Don't use sys.path manipulation
import sys
import os
sys.path.append(...)
```

