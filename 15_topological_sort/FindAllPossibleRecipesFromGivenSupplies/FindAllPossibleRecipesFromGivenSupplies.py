# Find All Possible Recipes from Given Supplies

from collections import defaultdict, deque


def find_recipes(recipes, ingredients, supplies):
    graph = defaultdict(list)
    in_degree = {r: 0 for r in recipes}
    result = []
    
    for i, recipe in enumerate(recipes):
        for ing in ingredients[i]:
            graph[ing].append(recipe)
            in_degree[recipe] += 1
    
    queue = deque(supplies)
    while queue:
        ing = queue.popleft()
        
        for recipe in graph[ing]:
            in_degree[recipe] -= 1
            if in_degree[recipe] == 0:
                result.append(recipe)
                queue.append(recipe)
        
    return result


# Test cases
if __name__ == "__main__":
    test_cases = [
        (["bread"], [["yeast", "flour"]], ["yeast", "flour", "corn"], ["bread"]),
        (["bread", "sandwich"], [["yeast", "flour"], ["bread", "meat"]], ["yeast", "flour", "meat"], ["bread", "sandwich"]),
        (["bread", "sandwich", "burger"], [["yeast", "flour"], ["bread", "meat"], ["sandwich", "meat", "bread"]], 
         ["yeast", "flour", "meat"], ["bread", "sandwich", "burger"]),
    ]
    
    print("Testing Find All Possible Recipes from Given Supplies:")
    all_passed = True
    for i, (recipes, ingredients, supplies, expected) in enumerate(test_cases, 1):
        result = find_recipes(recipes, ingredients, supplies)
        result_sorted = sorted(result)
        expected_sorted = sorted(expected)
        status = "✓" if result_sorted == expected_sorted else "✗"
        if result_sorted != expected_sorted:
            all_passed = False
        print(f"Test {i}: {status} find_recipes(...) = {result}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

