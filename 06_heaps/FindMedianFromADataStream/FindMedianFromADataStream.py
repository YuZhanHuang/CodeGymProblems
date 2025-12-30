# Find Median from a Data Stream

from heapq import *


class MedianOfStream:
    def __init__(self):
        self.min_heap_for_large = []
        self.max_heap_for_small = []

    def insert_num(self, num):
        if not self.max_heap_for_small or -self.max_heap_for_small[0] >= num:
            heappush(self.max_heap_for_small, -num)
        else:
            heappush(self.min_heap_for_large, num)

        if len(self.max_heap_for_small) - len(self.min_heap_for_large) > 1:
            heappush(self.min_heap_for_large, -heappop(self.max_heap_for_small))
        elif len(self.min_heap_for_large) > len(self.max_heap_for_small):
            heappush(self.max_heap_for_small, -heappop(self.min_heap_for_large))

    def find_median(self):
        if len(self.min_heap_for_large) == len(self.max_heap_for_small):
            return (self.min_heap_for_large[0] + (-self.max_heap_for_small[0])) / 2.0

        return -self.max_heap_for_small[0] / 1.0


# Test cases
if __name__ == "__main__":
    print("Testing Find Median from a Data Stream:")
    
    # Test 1
    median_stream = MedianOfStream()
    median_stream.insert_num(3)
    print(f"Test 1: Inserted 3, Median = {median_stream.find_median()}, expected 3.0")
    
    median_stream.insert_num(1)
    print(f"Test 2: Inserted 1, Median = {median_stream.find_median()}, expected 2.0")
    
    median_stream.insert_num(5)
    print(f"Test 3: Inserted 5, Median = {median_stream.find_median()}, expected 3.0")
    
    median_stream.insert_num(4)
    print(f"Test 4: Inserted 4, Median = {median_stream.find_median()}, expected 3.5")
    
    # Test 2
    median_stream2 = MedianOfStream()
    median_stream2.insert_num(1)
    median_stream2.insert_num(2)
    print(f"Test 5: Stream [1,2], Median = {median_stream2.find_median()}, expected 1.5")
    
    median_stream2.insert_num(3)
    print(f"Test 6: Stream [1,2,3], Median = {median_stream2.find_median()}, expected 2.0")

