# Fruit Into Baskets


def total_fruit(fruits):
    basket = {}  # fruit_type -> count in current window
    left = 0  # start of our window
    max_collected = 0

    # expand the window to the right, one tree at a time
    for right, f in enumerate(fruits):
        # add current fruit to basket
        basket[f] = basket.get(f, 0) + 1

        # if we have more than 2 types, shrink from the left
        while len(basket) > 2:
            left_fruit = fruits[left]
            basket[left_fruit] -= 1
            if basket[left_fruit] == 0:
                del basket[left_fruit]
            left += 1

        # update best answer
        window_size = right - left + 1
        if window_size > max_collected:
            max_collected = window_size

    return max_collected


# Driver code
def main():
    # Test case 1: Two types of fruits
    fruits1 = [1, 2, 1]
    result1 = total_fruit(fruits1)
    expected1 = 3  # All fruits can be collected
    print(f"Test 1: {result1 == expected1} (Expected: {expected1}, Got: {result1})")

    # Test case 2: Three types - need to choose best window
    fruits2 = [0, 1, 2, 2]
    result2 = total_fruit(fruits2)
    expected2 = 3  # [1,2,2] or [2,2,2]
    print(f"Test 2: {result2 == expected2} (Expected: {expected2}, Got: {result2})")

    # Test case 3: Multiple changes
    fruits3 = [1, 2, 3, 2, 2]
    result3 = total_fruit(fruits3)
    expected3 = 4  # [2,3,2,2]
    print(f"Test 3: {result3 == expected3} (Expected: {expected3}, Got: {result3})")

    # Test case 4: Only one type
    fruits4 = [3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]
    result4 = total_fruit(fruits4)
    expected4 = 5  # [1,2,1,1,2]
    print(f"Test 4: {result4 == expected4} (Expected: {expected4}, Got: {result4})")

    # Test case 5: Single fruit
    fruits5 = [5]
    result5 = total_fruit(fruits5)
    expected5 = 1  # Only one fruit
    print(f"Test 5: {result5 == expected5} (Expected: {expected5}, Got: {result5})")


if __name__ == "__main__":
    main()
