from sortedcontainers import SortedList
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.sorted_nums = SortedList(nums)
        self.top_k = k

    def add(self, val: int) -> int:
        self.sorted_nums.add(val)
        return self.sorted_nums[-1 * self.top_k]
