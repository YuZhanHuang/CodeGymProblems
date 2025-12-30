# Random Pick with Weight

import random


class RandomPickWithWeight:

    def __init__(self, weights):
        # The weights array, consisting of integers, is passed to the constructor
        self.running_weight = []
        total = 0
        for weight in weights:
            total += weight
            self.running_weight.append(total)
        self.total = total

    def pick_index(self):
        pick = random.randint(1, self.total)
        start, end = 0, len(self.running_weight) - 1

        while start < end:
            mid = start + (end - start) // 2
            if pick > self.running_weight[mid]:
                start = mid + 1
            else:
                end = mid

        return start


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4, 5]),
        ([1, 12, 23, 34, 45]),
    ]
    
    print("Testing Random Pick with Weight:")
    for i, weights in enumerate(test_cases, 1):
        counter = 10000
        sol = RandomPickWithWeight(weights)
        counts = [0] * len(weights)
        
        for _ in range(counter):
            index = sol.pick_index()
            counts[index] += 1
        
        print(f"\nTest {i}: weights = {weights}")
        total_weight = sum(weights)
        for j in range(len(weights)):
            actual_freq = (counts[j] / counter) * 100
            expected_freq = (weights[j] / total_weight) * 100
            print(f"  Index {j}: {actual_freq:.2f}% (expected ~{expected_freq:.2f}%)")
    
    print("\nNote: Random tests - frequencies should be close to expected values")

