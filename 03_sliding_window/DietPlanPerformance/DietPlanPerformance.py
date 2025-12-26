def diet_plan_performance(calories, k, lower, upper):
    curr_sum = sum(calories[0:k])
    scores = 0

    if curr_sum < lower:
        scores -= 1
    elif curr_sum > upper:
        scores += 1

    for i in range(k, len(calories)):
        curr_sum += calories[i] - calories[i - k]

        if curr_sum < lower:
            scores -= 1
        elif curr_sum > upper:
            scores += 1

    return scores


# Driver code
def main():
    # Test case 1: Mixed performance (some windows above, some below, some in range)
    calories1 = [1, 2, 3, 4, 5]
    k1 = 1
    lower1 = 3
    upper1 = 3
    result1 = diet_plan_performance(calories1, k1, lower1, upper1)
    expected1 = -2  # [1<3:-1, 2<3:-1, 3=3:0, 4>3:+1, 5>3:+1] = -2+0+1+1 = 0... wait
    # Let me recalculate: 1<3(-1), 2<3(-1), 3 in [3,3](0), 4>3(+1), 5>3(+1) = -2+2 = 0
    expected1 = 0
    print(f"Test 1: {result1 == expected1} (Expected: {expected1}, Got: {result1})")

    # Test case 2: All windows within range
    calories2 = [3, 2, 2, 3, 3, 3]
    k2 = 2
    lower2 = 0
    upper2 = 10
    result2 = diet_plan_performance(calories2, k2, lower2, upper2)
    expected2 = 0  # All sums (5,4,5,6,6) are in range [0,10]
    print(f"Test 2: {result2 == expected2} (Expected: {expected2}, Got: {result2})")

    # Test case 3: All windows below lower threshold
    calories3 = [1, 1, 1, 1, 1]
    k3 = 2
    lower3 = 5
    upper3 = 10
    result3 = diet_plan_performance(calories3, k3, lower3, upper3)
    expected3 = -4  # 4 windows, all with sum=2 < 5
    print(f"Test 3: {result3 == expected3} (Expected: {expected3}, Got: {result3})")

    # Test case 4: All windows above upper threshold
    calories4 = [6, 5, 0, 0]
    k4 = 2
    lower4 = 1
    upper4 = 3
    result4 = diet_plan_performance(calories4, k4, lower4, upper4)
    expected4 = 1  # Windows: 11>3(+1), 5 in [1,3](0), 0<1(-1) = 1+0-1 = 0... wait
    # 6+5=11>3(+1), 5+0=5>3(+1), 0+0=0<1(-1) = 1+1-1 = 1
    expected4 = 1
    print(f"Test 4: {result4 == expected4} (Expected: {expected4}, Got: {result4})")

    # Test case 5: k equals array length (only one window)
    calories5 = [6, 13, 8, 7, 10, 1]
    k5 = 6
    lower5 = 5
    upper5 = 37
    result5 = diet_plan_performance(calories5, k5, lower5, upper5)
    expected5 = 1  # Sum = 45 > 37, so +1
    print(f"Test 5: {result5 == expected5} (Expected: {expected5}, Got: {result5})")


if __name__ == "__main__":
    main()
