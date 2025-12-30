# First Bad Version

class API:
    def __init__(self, first_bad):
        self.first_bad = first_bad
    
    def is_bad(self, v):
        return v >= self.first_bad


version_api = None


def is_bad_version(v):
    return version_api.is_bad(v)


def first_bad_version(n):
    start, end = 1, n
    count = 0

    while start < end:
        mid = (start + end) // 2
        check = is_bad_version(mid)
        count += 1
        # 找到壞掉
        if check is True:
            # 注意 ！！！ end = mid 正確 end = mid - 1 錯誤 原因
            # 當你找到錯誤時，要以他當end取找出上一個還是好的版本
            end = mid
        else:
            start = mid + 1

    return start, count


# Test cases
if __name__ == "__main__":
    test_cases = [
        (5, 4),  # n=5, first_bad=4
        (1, 1),  # n=1, first_bad=1
        (100, 50),  # n=100, first_bad=50
    ]
    
    print("Testing First Bad Version:")
    all_passed = True
    for i, (n, first_bad) in enumerate(test_cases, 1):
        version_api = API(first_bad)
        result, count = first_bad_version(n)
        status = "✓" if result == first_bad else "✗"
        if result != first_bad:
            all_passed = False
        print(f"Test {i}: {status} first_bad_version({n}) = {result} (calls: {count}), expected {first_bad}")
    
    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed!'}")

