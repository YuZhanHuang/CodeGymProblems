# Gas Stations

def gas_station_journey(gas, cost):
    if sum(cost) > sum(gas):
        return -1

    current_gas, start_idx = 0, 0
    for i in range(len(gas)):
        current_gas = current_gas + gas[i] - cost[i]
        if current_gas < 0:
            start_idx = i + 1
            current_gas = 0

    return start_idx


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4, 5], [3, 4, 5, 1, 2], 3),
        ([2, 3, 4], [3, 4, 3], -1),
    ]
    
    print("Testing Gas Stations:")
    all_passed = True
    for i, (gas, cost, expected) in enumerate(test_cases, 1):
        result = gas_station_journey(gas, cost)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status} gas_station_journey(gas={gas}, cost={cost}) = {result}, expected {expected}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

